# hometown_analysis

An analysis of immigration to my hometown (Great Neck, NY) over time. The analysis focuses on two waves of immigration:

  1. Immigration from Iran, which began during the Iranian Revolution of 1978.
  2. Immigration from East Asia, which began later.

Another goal is for the repository to serve as a template for others looking to do a similar analysis.

## Methodology

This repo uses the Python package `censusdis` to access data from the Census Bureau's American Community Survey (ACS). 
The geography I chose is the School District I attended as a child (Great Neck Union Free School District). 

ACS data on School Districts is published in "5-year estimates". The first 5-year estimate was published in 2009 and the last was published in 2023. You are not supposed to compare overlapping 5-year periods, so I chose to compare the first year, the last year and the year in the middle (2009, 2016 and 2023).

## Results

The analytical results are captured in four Jupyter notebooks:

  * [05-nativity.ipynb](./05-nativity.ipynb). "Nativity" is the term Census uses for whether a resident was born in the US or another country. Analyzing nativity over time seems like a reasonable proxy for immigration.
  * [06-place-of-birth.ipynb](./06-place-of-birth.ipynb). Census asks residents which country they were born in. This allowed me to compare immigration from Iran vs. East Asia over time. 
  * [07-race.ipynb](./07-race.ipynb). I was curious whether immigration changed the racial composition of my hometown.
  * [08-china-breakdown.ipynb](./08-china-breakdown.ipynb). Someone asked whether it was possible to subdivide immigration from China into Taiwan,  Hong Kong and Mainland China. It is, and this workbook shows how.

## What About ...?

Analyses like this often cause people to ask: "What about ...?"

Rather than try to answer every possible question, I created a guide on how to modify the analysis to suit your own needs. It starts with instructions on how to recreate the virtual environment I used to create the analysis. It also discusses issues specific to analyzing Census data such as choosing a geography and tables.

See [DEVELOPER.md](./DEVELOPER.md) to learn more. 

### Future Work

This analysis is limited by the start date of the first 5-year ACS (2009). Two potential ways to go further back in time are:

  1. Combine ACS data with data from the 2000 Decennial Census. I believe that this data is available via the Census API, although I have not worked with it before.
  2. Combine ACS data with data from pre-2000 Decennial Censuses. I believe that this data is not available via the Census API, but can be accessed via IPUMS.

If you would like to learn about any future development in this project please [subscribe](https://arilamstein.com/) to my newsletter.

### Blog Posts

In addition to the above notebooks, you may enjoy these blog posts about this project. They are presented in chronological order and reflect milestones in the project.
   * [New Project: hometown_analysis](https://arilamstein.com/blog/2025/01/13/new-project-hometown_analysis/)
   * [New Python Functions for Working with Multi-Year ACS Data](https://arilamstein.com/blog/2025/01/29/new-python-functions-for-working-with-multi-year-acs-data/)
   * [New Parameter to `download_multiyear`](https://arilamstein.com/blog/2025/02/21/new-parameter-to-download_multiyear/)
