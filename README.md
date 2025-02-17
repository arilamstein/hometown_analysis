# hometown_analysis

An attempt to understand how the demographics of my hometown (Great Neck, NY) have changed during my lifetime (1978-Present). I am particularly interested in measuring the impact of two waves of immigration:

  1. Immigration from Iran due to the Iranian Revolution of 1978-1979.
  2. Immigration from Asia.

While only one location is being analyzed, and through only one specific lens, my intention is to write the code in such a way that it can be reused by others for similar purposes.

I view this project as having 2 distinct phases:
  1. Analyzing data from the [American Community Survey (ACS) 5-Year Estimates](https://en.wikipedia.org/wiki/American_Community_Survey). 
   I have prior experience working with this dataset, which is why it is a natural place to start. However, it only goes back to 2010.

  2. Combining ACS data with data from the 1980, 1990 and 2000 Decennial Censuses. I have not worked with these datasets before, 
  but I believe that they can be accessed via [IPUMS](https://www.ipums.org/).

I am currently working on Phase 1, and am am recording my progress using Jupyter Notebooks:

Getting Started:
  * [01-geographic-choice.ipynb](./01-geographic-choice.ipynb)
  * [02-geographic-stability.ipynb](./02-geographic-stability.ipynb)
  * [03-table-selection-and-ingestion.ipynb](./03-table-selection-and-ingestion.ipynb)
  * [04-multi-year-data.ipynb](./04-multi-year-data.ipynb)

Analysis:
  * [05-nativity.ipynb](./05-nativity.ipynb)