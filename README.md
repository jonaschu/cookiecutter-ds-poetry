# Cookiecutter Data Science with Poetry

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work. Using Poetry for dependency management_


#### [Project homepage](https://jonaschu.github.io/cookiecutter-ds-poetry/)


## Requirements to use the cookiecutter template:
To make sure, that the required python version is installed, we will use conda for enviroment creation, but Poetry for managing dependecies. 

To use the template properly, you must have ...
 - ... *Poetry* installed. Follow the instructions [here](https://python-poetry.org/docs/#installation) to install Poetry.
 - ... *Anaconda* or *[miniconda](https://docs.conda.io/en/latest/miniconda.html)* installed
 - ... the [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) installed in a enviroment (in a extra one is recommended): 
 
Here is how you create a extra cookiecutter enviroment with conda:
``` bash
conda create -n cookiecutter cookiecutter -c conda-forge
conda activate cookiecutter
```

## To start a new project, run:
*create the project stucture base on this template*
``` bash
# enviroment with cookiecutter installed is activated
cookiecutter -c v1 https://github.com/jonaschu/cookiecutter-ds-poetry
```
Answer the questions.
``` bash
# switch in newly create project folder
cd <project-name>
```

*Continue to follow the installation process in the README.md of the newly created project.*



## The resulting directory structure

The directory structure of your new project looks like this: 

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
├── <PACKAGE_NAME>         <- Source code for use in this project.
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
<p><small>Inspired by <a target="_blank" href="https://drivendata.github.io/cookiecutter-ds/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
