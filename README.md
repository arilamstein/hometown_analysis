# hometown_analysis

An analysis of immigration to my hometown (Great Neck, NY) over time. During recent visits people said that the town had changed a lot since I left. This repository attempts to measure that change. 

Additionally, this repo attempts to serve as a template for others looking to do similar analyses.

## Methodology

I used the Python package `censusdis` to access data from the Census Bureau's American Community Survey (ACS). The geography I chose is the School District I attended as a child (Great Neck Union Free School District). 

ACS data on School Districts is published in "5-year estimates". The first 5-year estimate was published in 2009 and the last was published in 2023. You are not supposed to compare overlapping 5-year periods, so I chose to compare the first year, the last year and the year in the middle (2009, 2016 and 2023).

You can learn more about my design decisions in [DEVELOPER.md](./DEVELOPER.md).

## Results

At a high level: overall immigration increased slightly, but the location where those immigrants came from changed significantly. The following notebooks go into more detail:

  * [05-nativity.ipynb](./05-nativity.ipynb) shows that the percentage of the town that is "Foreign-Born" increased only sightly, from 30% to 32%.
  * [06-place-of-birth.ipynb](./06-place-of-birth.ipynb) shows that the country which immigrants came from changed significantly. In 2009 Iran was, by far, the largest source of immigration. By 2023 that changed to China. Additionally, the number of immigrants from Korea increased by 66%. In short: immigration shifted from Iran to Eastern Asia.  
  * [07-race.ipynb](./07-race.ipynb). Not surprisingly, the increased immigration from Eastern Asia changed the racial composition of the town. The percentage of residents who are "Asian alone" increased from 11% to 27%. 

## What About ...?

Analyses like this often cause people to ask: "What about ...?"

I designed this repository to be easy to modify. If you would like to tweak this analysis to answer a slightly different question (such as a different geography, or different tables), please read [DEVELOPER.md](./DEVELOPER.md). 

## Future Work

This analysis is limited by the start date of the first 5-year ACS (2009). Two potential ways to go further back in time are:

  1. Combine ACS data with data from the 2000 Decennial Census. I believe that this data is available via the Census API, although I have not worked with it before.
  2. Combine ACS data with data from pre-2000 Decennial Censuses. I believe that this data is not available via the Census API, but can be accessed via IPUMS.

If you would like to be notified about future development then please subscribe to my newsletter. The signup form is on the bottom of my [homepage](https://arilamstein.com/).

## Blog Posts

In addition to the above notebooks I wrote three blog posts about this project. They are presented in chronological order and reflect milestones in the project.
   * [New Project: hometown_analysis](https://arilamstein.com/blog/2025/01/13/new-project-hometown_analysis/)
   * [New Python Functions for Working with Multi-Year ACS Data](https://arilamstein.com/blog/2025/01/29/new-python-functions-for-working-with-multi-year-acs-data/)
   * [New Parameter to `download_multiyear`](https://arilamstein.com/blog/2025/02/21/new-parameter-to-download_multiyear/)
