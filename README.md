# hometown_analysis

An attempt to understand how the demographics of my hometown (Great Neck, NY) have changed during my lifetime (1978-Present). I am particularly interested in measuring the impact of two waves of immigration:

  1. Immigration from Iran due to the Iranian Revolution of 1978-1979.
  2. Immigration from Asia.

While only one location is being analyzed, and through only one specific lens, my intention is to write the code in such a way that it can be reused by others for similar purposes.

I view this project as having 3 distinct phases. Each phase corresponds to a distinct location for data:
  1. Using data from the [American Community Survey (ACS) 5-Year Estimates](https://en.wikipedia.org/wiki/American_Community_Survey). Unfortunately this dataset only goes back to 2010.
  2. Adding data from the 2000 Decennial Census, which is available via the Census API.
  3. Adding data from the Decennial Censuses for 1980 and 1990, which I expect to get from [IPUMS](https://www.ipums.org/).

I am currently working on Phase 1. Milestones in this project are recorded in Jupyter Notebooks:
  * [01-geographic-choice.ipynb](./01-geographic-choice.ipynb)
  * [02-geographic-stability.ipynb](./02-geographic-stability.ipynb)
  * [03-tables.ipynb](./03-tables.ipynb)