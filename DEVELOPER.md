My hope is that this project inspires at least one person to use Python to explore ACS data.  

All code in this repo is released under the MIT License. This means that you are free to fork the repository and modify it to answer whatever questions you have.

## Installation
I used `uv` to manage my virtual environment while developing this project. To recreate my environment:
1. Clone this repository
2. Install uv ([link](https://docs.astral.sh/uv/))
3. In the project directory type `uv sync`. This will create a virtual environment with the project's dependencies in `.venv` 
4. Type `source .venv/bin/activate` to activate the virtual environment

You should then be able to execute all the code in the notebooks locally. I personally used VS Code to develop the notebooks and `utils.py`. 

## Working with Census Data

As you modify the analysis you will likely have questions about Census-specific topics. I created four Notebooks that might help you:

  * [01-geographic-choice.ipynb](./01-geographic-choice.ipynb) explains how I chose the School District geography.
  * [02-geographic-stability.ipynb](./02-geographic-stability.ipynb) shows how I verified that the geography was stable over time.
  * [03-table-selection-and-ingestion.ipynb](./03-table-selection-and-ingestion.ipynb) shows how I decided which tables to analyze.
  * [04-multi-year-data.ipynb](./04-multi-year-data.ipynb) walks through technical issues I encountered, and the code I wrote to solve them.

If you wind up using this repo to conduct your own analysis, I would love to know. You can contact me via the contact form on my [website](https://arilamstein.com/).
