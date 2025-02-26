My hope is that this project inspires at least one other person to use Python to explore ACS data. I often describe the ACS as a national treasure, and feel that it is not sufficently appreciated by data scientists. 

All code in this repo is released under the MIT License. This means that you are free to fork the repository and modify it to answer whatever questions interest you.

### Installation
The project's dependencies are listed in two files: `pytproject.toml` and `uv.lock`. I recommending using `uv` to recreate the exact environment I had when developing the project. To do so:
1. Clone this repository
2. Install uv ([link](https://docs.astral.sh/uv/))
3. In the project directory type `uv sync`. This will create a virtual environment based on the project's dependencies 
4. Type `source .venv/bin/activate` to activate the virtual environment

You should then be able to execute all the code in the notebooks locally. I personally used VS Code to develop the notebooks and `utils.py`. 

### Working with Census Data

As you think about modifying the analysis to your own needs you will likely have questions about Census-specific topics. I created four Notebooks that might help you:

  * [01-geographic-choice.ipynb](./01-geographic-choice.ipynb). How do you define a "hometown" using Census Bureau geography?
  * [02-geographic-stability.ipynb](./02-geographic-stability.ipynb). Will an analysis over time be measuring the same area?
  * [03-table-selection-and-ingestion.ipynb](./03-table-selection-and-ingestion.ipynb). Which ACS tables best answer the specific questions I have?
  * [04-multi-year-data.ipynb](./04-multi-year-data.ipynb). How to use the functions I wrote to download and analyze multiple years worth of Census data in a single line of code.

If you wind up using this repo to conduct your own analysis, I would love to know. You can contact me via the contact form on my [website](https://arilamstein.com/).
