# hometown_analysis

An analysis of immigration to my hometown (Great Neck, NY) over time. The analysis focuses on two waves of immigration:

  1. Immigration from Iran, which began during the Iranian Revolution of 1978.
  2. Immigration from East Asia, which began later.

This repo is also intended to serve as a starting off point for anyone who wants to analyze demographic data in Python. 

### Methodology

This repo uses the Python package `censusdis` to access data from the Census Bureau's American Community Survey (ACS). 
The geography I chose is the School District I attended as a child (Great Neck Union Free School District). 

ACS data on School Districts is published in what are known as "5-year estimates". The first 5-year estimate was published in 
2009 and the last was published in 2023. You are not supposed to compare overlapping 5-year periods, so we can only compare 3 datasets. 
I chose to compare the first year, the last year and the year in the middle (2009, 2016 and 2023).

### Results

The analytical results are captured in 4 Jupyter notebooks:

  * [05-nativity.ipynb](./05-nativity.ipynb). "Nativity" is the term Census uses for whether a resident was born in the US or another country. Analyzing nativity over time seems like a reasonable proxy for immigration.
  * [06-place-of-birth.ipynb](./06-place-of-birth.ipynb). Census asks residents which country they were born in. This allowed me to compare immigration from Iran vs. East Asia over time. 
  * [07-race.ipynb](./07-race.ipynb). I was curious whether immigration changed the racial composition of my hometown.
  * [08-china-breakdown.ipynb](./08-china-breakdown.ipynb). Someone asked whether it was possible to subdivide immigration from China into Taiwan,  Hong Kong and Mainland China. It is, and this workbook shows how.

### Modifying the Analysis

My hope is that this project inspires at least one other person to use Python to explore ACS data. I often describe the ACS as a national treasure, and feel that it is not sufficently appreciated by data scientists. 

All code in this repo is released under the MIT License. This means that you are free to fork the repository and modify it to answer whatever demographic questions interest you.

The project's dependencies are listed in two files: `pytproject.toml` and `uv.lock`. I recommending using `uv` to recreate the exact environment I had when developing the project. To do so type `uv sync` from the project directory activate the virtual environment uv created by typing `source .venv/bin/activate`.

You should then be able to execute all the code in the notebooks locally.

As you think about modifying the analysis to your own needs you will likely run into issues such as:
1. Choosing a geography
2. Verifying that the boundaries of that geography have not changed significantly over time
3. Choosing which tables to analyze 
4. Figuring out the best way to analyze multiple years of data

As I worked through these issues I recording my solutions in the form of Notebooks. Reading these notebooks will likely help you:

  * [01-geographic-choice.ipynb](./01-geographic-choice.ipynb). How do you define a "hometown" using Census Bureau geography?
  * [02-geographic-stability.ipynb](./02-geographic-stability.ipynb). Will an analysis over time be measuring the same area?
  * [03-table-selection-and-ingestion.ipynb](./03-table-selection-and-ingestion.ipynb). Which ACS tables best answer the specific questions I have?
  * [04-multi-year-data.ipynb](./04-multi-year-data.ipynb). How to use the functions I wrote to download and analyze multiple years worth of Census data in a single line of code.

If you wind up using this repo to conduct your own analysis, I would love to know. You can contact me via the contact form on my [website](https://arilamstein.com/).

### Future Work

This work is primarily limited by the start date of the first 5-year ACS (2009). Two potential ways to go further back in time are:

  1. Combine the data above with data from the 2000 Decennial Census. I believe that this data is available via the Census API, although I have never worked with it myself.
  2. Combine the data above with data from pre-2000 Decennial Censuses. I believe that this data is not available via the Census API, and so I would have to get it from somewhere else (for example IPUMS). 

### Blog Posts

In addition to the above notebooks, you may like reading three blog posts about this project:
   * [New Project: hometown_analysis](https://arilamstein.com/blog/2025/01/13/new-project-hometown_analysis/), January 13, 2025
   * [New Python Functions for Working with Multi-Year ACS Data](https://arilamstein.com/blog/2025/01/29/new-python-functions-for-working-with-multi-year-acs-data/), January 29, 2025
   * [New Parameter to `download_multiyear`](https://arilamstein.com/blog/2025/02/21/new-parameter-to-download_multiyear/), February 21, 2025
