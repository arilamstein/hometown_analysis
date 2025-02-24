# hometown_analysis

An attempt to understand how the demographics of my hometown (Great Neck, NY) changed during my lifetime (1978-Present). I am particularly interested in measuring two waves of immigration:

  1. Immigration from Iran, which began during the Iranian Revolution of 1978.
  2. Immigration from East Asia, which began later.

The analysis is done in a series of Jupyter Notebooks and released under the MIT License. I encourage you to fork this repo and edit the variables to answer similar questions about your own hometown! If you wind up using this repo to conduct your own analysis, I would love to know. You can contact me via the contact form on my [website](https://arilamstein.com/).

My approach is to use the Python package `censusdis` to download American Community Survey (ACS) 5-Year Estimates from the Census Bureau API. A limitation of this approach is that the first 5-year ACS was published in 2009. You are not supposed to compare overlapping years. This gives us just 3 datapoints: 2009, 2014 and 2019. (The 2024 5-year ACS is scheduled for release at the end of the 2025).

### Getting Started

Prior to analyzing any data I did the following:
  * [01-geographic-choice.ipynb](./01-geographic-choice.ipynb). How do you define a "hometown" using Census Bureau geography?
  * [02-geographic-stability.ipynb](./02-geographic-stability.ipynb). Will an analysis over time be measuring the same area?
  * [03-table-selection-and-ingestion.ipynb](./03-table-selection-and-ingestion.ipynb). Which ACS tables best answer the specific questions I have?
  * [04-multi-year-data.ipynb](./04-multi-year-data.ipynb). I was surprised that neither the Census API nor censusdis have built-in support for downloading and analyzing multiple year's worth of ACS data. I implemented my own solution and this workbook demonstrates how to use it.

### Analysis

After completing the above I was able to start trying to answer my original question:
  * [05-nativity.ipynb](./05-nativity.ipynb). "Nativity" is the term for whether a resident was born in the US or another country. Analyzing nativity over time seems like a reasonable proxy for immigration.
  * [06-place-of-birth.ipynb](./06-place-of-birth.ipynb). Census asks residents which country they were born in. This allows us to compare immigration from Iran vs. East Asia over time. 
  * [07-race.ipynb](./07-race.ipynb). Has the immigration from Asia changed the racial composition of my hometown?
  * [08-china-breakdown.ipynb](./08-china-breakdown.ipynb). A friend asked whether it was possible to subdivide immigration from China into Taiwan,  Hong Kong and Mainland China. It is, and this workbook shows how.

### Further Reading

In addition to the above notebooks, I have written three blog posts about this project:
   * [New Project: hometown_analysis](https://arilamstein.com/blog/2025/01/13/new-project-hometown_analysis/), January 13, 2025
   * [New Python Functions for Working with Multi-Year ACS Data](https://arilamstein.com/blog/2025/01/29/new-python-functions-for-working-with-multi-year-acs-data/), January 29, 2025
   * [New Parameter to `download_multiyear`](https://arilamstein.com/blog/2025/02/21/new-parameter-to-download_multiyear/), February 21, 2025
