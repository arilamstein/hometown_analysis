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


def warn_variable_changes(df, dataset, vintages, group):
    years = df["Year"].unique()

    for col in df.columns:
        # Not all columns contain actual ACS data. The ones we care about have names like
        # B01001_001E. That is, they start with the group name.
        if not col.startswith(group):
            continue

        unique_labels_for_variable = get_unique_labels_for_variable(
            dataset, col, vintages
        )

        if len(unique_labels_for_variable) > 1:
            print(f"Warning: {col} has had multiple labels over the selected years:")
            for label, years in unique_labels_for_variable.items():
                print(f"\t'{label}' in {years}")


def download_multiyear(
    dataset, vintages, group, rename_vars=True, drop_cols=True, **kwargs
):

    df = None

    for vintage in vintages:
        # This loop can take a while, so provide feedback to the user
        print(".", end="", flush=True)

        df_new = ced.download(
            dataset=dataset,
            vintage=vintage,
            group=group,
            **kwargs,
        )

        df_new["Year"] = vintage

        if df is None:
            df = df_new
        else:
            df = pd.concat([df, df_new])

    # In the ACS, Sometimes the same variable is used for different things in different years.
    # For an example see https://arilamstein.com/blog/2024/05/28/creating-time-series-data-from-the-american-community-survey-acs/
    # This code alerts users of any variables which have had different labels over time.
    warn_variable_changes(df, dataset, vintages, group)

    if drop_cols:
        df = df[[col for col in df.columns if col.startswith(group) or col == "Year"]]

    if rename_vars:
        df = df.rename(columns=name_mapper(group=group, vintage=vintages[-1]))

    return df


def graph_multiyear(df, title, yaxis_title, y_cols=None, set_pio_default_renderer=True):
    """
    Create a (multi-line) graph of time series data using plotly.

    Parameters
    ----------
    df : dataframe
        Must have a column called 'Year' which will serve as the x-axis.
    title : str
        Title for the graph.
    yaxis_title : str
        Title for the y-axis.
    y_cols : str | None
        A list of columns in `df` to create lines for. If None then will graph all
        columns except "Year".
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

    df = download_multiyear(
        dataset=ACS5,
        vintages=[2010, 2015, 2020],
        group="B05012",
        state=NY,
        school_district_unified="12510",
    )
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

    if not y_cols:
        y_cols = [col for col in df.columns if col != "Year"]

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
