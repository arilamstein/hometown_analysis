from collections import defaultdict
import pandas as pd

import censusdis.data as ced
from censusdis.datasets import ACS5

import plotly.graph_objects as go
import plotly.io as pio


def name_mapper(group, vintage):
    def inner(variable: str):
        """Map from the variables we got back to their labels."""
        if variable.startswith(group):
            # Look up details of the particular variable:
            vars = ced.variables.search(ACS5, vintage, group_name=group, name=variable)
            # Get the label and parse out the part we want:
            label = vars.iloc[0]["LABEL"]
            return label.split("!")[-1].split(":")[0]
        else:
            # Not in the group we are interested in, so leave it as is.
            return variable

    return inner


def get_unique_labels_for_variable(acs, variable, years):
    """
    Return all labels the ACS has used for a given variable.

    Note that the ACS sometimes changes the labels of a variable. Sometimes these changes are minor,
    and sometimes the same variable is used for something completely different. This function is designed to
    facilitate doing this check over multiple years.

    For example, B08006_017E in 2005 had label 'Estimate!!Total!!Motorcycle'. But in 2006 it switched to
    'Estimate!!Total!!Worked at home'. And in 2019 it changed to 'Estimate!!Total:!!Worked from home'.

    Parameters:
    - acs: The ACS to use. Ex. censusdis.datasets.ACS1)
    - variable: The variable in question. Ex. 'B01001_001E'
    - years: An iterable of years to use. Ex. [2005, 2006, 2007]

    Returns:
    - A dict where each key is a label, and each value is a list of years that key has been used.

    Note: If the dict returned is of length 1, then the variable has only ever had 1 label.
    """
    labels = defaultdict(list)

    for year in years:
        label = ced.variables.get(acs, year, variable)["label"]
        labels[label].append(year)

    return labels


def get_variables_used(df):
    non_variable_columns = ["NAME", "COUNTY_NAME", "STATE_NAME", "YEAR"]
    return [
        one_column
        for one_column in df.columns
        if one_column not in non_variable_columns
    ]


def get_years_variable_used(df, variable):
    return df[df[variable].notna()]["YEAR"].unique()


def print_labels_for_variables_over_time(df):
    variables_used = get_variables_used(df)

    for variable in variables_used:
        years_variable_used = sorted(get_years_variable_used(df, variable))
        unique_labels_for_variable = get_unique_labels_for_variable(
            ACS5, variable, years_variable_used
        )

        if len(unique_labels_for_variable) == 1:
            print(f"{variable} has only 1 label")
        else:
            print(f"{variable} has the following labels:")
            for label, years in unique_labels_for_variable.items():
                print(f"\t'{label}' in years {years}")


def graph_ts_df(df, y_cols, title, yaxis_title, set_pio_default_renderer=True):
    """
    Create a (multi-line) graph of time series data using plotly.

    Parameters
    ----------
    df : dataframe
        Must have a column called 'Year' which will serve as the x-axis.
    y_cols : str
        A list of columns in `df` to create lines for.
    title : str
        Title for the graph.
    yaxis_title : str
        Title for the y-axis.
    set_pio_default_renderer : bool
        By default plotly generates interactive graphs. Unfortunately, these graphs
        do not render when notebooks are viewed on github. Setting this option to
        True (the default) sets plotlyio.renderers.default="vscode+png", which also
        generates png versions of the plots. This allows notebooks which use this
        function to have their graphs viewable on github.

    Returns
    -------
    NoneType

    Examples
    --------
    import pandas as pd

    YEARS = [2010, 2015, 2020]
    GROUP = "B05012"
    df = None

    for year in YEARS:
        # This loop can take a while, so provide feedback to the user
        print(".", end="", flush=True)

        df_new = ced.download(
            dataset=ACS5,
            vintage=year,
            group=GROUP,
            state=NY,
            school_district_unified="12510",
        )

        df_new["Year"] = year

        if df is None:
            df = df_new
        else:
            df = pd.concat([df_new, df])

    df = df.rename(columns=name_mapper(group=GROUP, vintage=2020))
    graph_ts_df(
        df,
        ["Total", "Native", "Foreign-Born"],
        "Population by Nativity in Great Neck School District",
        "Population",
    )
    """

    # By default plotly graphs are interactive. While this is great locally, they do not render
    # on github. This allows static version of the graphs to appear on github in addition to seeing
    # interactive versions locally. See https://github.com/plotly/plotly.py/issues/931#issuecomment-2098209279
    if set_pio_default_renderer:
        pio.renderers.default = "vscode+png"

    colorblind_palette = [
        "#E69F00",
        "#56B4E9",
        "#009E73",
        "#F0E442",
        "#0072B2",
        "#D55E00",
        "#CC79A7",
    ]

    fig = go.Figure()

    for idx, y_col in enumerate(y_cols):
        color = "black" if y_col == "Total" else colorblind_palette[idx]
        fig.add_trace(
            go.Scatter(
                x=df["Year"],
                y=df[y_col],
                mode="lines+markers",
                name=y_col,
                line=dict(color=color),
                hovertemplate="Year: %{x}<br>" + y_col + ": %{y:,}<extra></extra>",
            )
        )

    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Year",
        yaxis_title=yaxis_title,
        xaxis=dict(
            tickmode="array",
            tickvals=df["Year"],
            ticktext=[str(year) for year in df["Year"]],
        ),
    )

    fig.show()
