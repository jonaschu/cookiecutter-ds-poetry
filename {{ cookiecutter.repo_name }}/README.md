# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation
Here we will use conda for setting up an enviroment with a specific Python version ({{cookiecutter.python_version}}) and poetry for all package management. 

### Prerequisite

You need have pre-installed:
- **Poetry**, else follow the instructions [here](https://python-poetry.org/docs/#installation) to install Poetry.
- Anaconda or [miniconda](https://docs.conda.io/en/latest/miniconda.html).


### Create a virtual conda python enviroment
``` bash
# create base enviroment with specific python version
conda create -n "{{cookiecutter.repo_name}}-py{{cookiecutter.python_version}}" python={{cookiecutter.python_version}}
# next activate the enviroment
conda activate "{{cookiecutter.repo_name}}-py{{cookiecutter.python_version}}"
```
``` bash
# install dependencies in conda enviroment.
poetry install
```

## Usage
``` bash
# install dependencies in conda enviroment.
conda activate "{{cookiecutter.repo_name}}-py{{cookiecutter.python_version}}"
# activate poetry shell
poetry shell
```


## Project Organization
```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, Images etc.
│
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── {{cookiecutter.repo_name}}         <- Source code for use in this project.
│   ├── __init__.py    <- Makes {{cookiecutter.repo_name}} a Python module
│   │
│   ├── etl            <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── poetry.toml        <- local config file for poetry
│
└── pyproject.toml     <- file to define the poetry project
```

--------
<p><small>Project based on <a target="_blank" href="https://jonaschu.github.io/cookiecutter-ds-poetry/">Cookiecutter Data Science Poetry</a>, inspired by <a target="_blank" href="https://drivendata.github.io/cookiecutter-ds/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


<p><small>Project based on the cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
