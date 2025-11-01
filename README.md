# DDE-repo

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Created for ITMO's Data Driven Engineering homework

Gas Chromatography ETL

## Project Organization

```
├── Makefile           <- Makefile with convenience commands.
├── README.md          <- Project documentation.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── cache              <- Pictures from README
│
├── experiments        <- Some code experiments.
│   ├── api_reader.py           <- Parsing API script.
│   └── README.md               <- Parsing documentation.
│
├── notebooks          <- Jupyter notebooks.
│   └── dtypes.ipynb            <- Dataset research for matching dtypes
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         gc_etl and configuration for tools like black
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   │
│   ├── EDA.ipynb      <- Exploratory Data Analysis
│   │
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── environment.yml    <- The requirements file for reproducing the analysis environment
│
├── setup.cfg          <- Configuration file for flake8
│
├── experiments/       <- Some experiments
│   │
│   ├── api_reader.py           <- Parsing API script
│   │
│   └── README.md               <- Parsing documentation
│
└── gc_etl   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes gc_etl a Python module
    ├── extract.py              <- Data extract (from local or GDrive)
    ├── transform.py            <- Data typing, cleaning
    ├── load.py                 <- Data load (to local or DB or both)
    └── main.py                 <- Main module (orchestrator)
```

---

### Data
Dataset contains information about **gas chromatography (GC)**

[Link](https://drive.google.com/file/d/1twkoRrET6qJqgXPzG9jzrMqQikSzi1Ok/view?usp=sharing) to dataset  
Dataset info:
![read_data_result](cache/read_data_result.png)
Dataset dtypes:
![data_dtypes](cache/data_processing_result.png)

### Installing Dependencies
1. Download conda
2. Clone repository ```git clone https://github.com/Eternal-insomnia/DDE-repo.git```
3. Move into repository ```cd DDE-repo```
4. Install dependencies: ```conda env create -f environment.yml``` or ```make create_environment```

---

### CLI-argumets
This project has a few CLI-arguments:  
1. `-ext-l` or `--extract-local` with CSV-file name (e.g. `-ext-l test.csv`). Create `data/raw` folder in the project directory. Move .csv file into `data/raw` folder
2. `-ext-g` or `--extract-gdrive` with CSV-file Google Drive id (e.g. `-ext-g 14jdCxjCsB0NT5ExKhWByxMiNHvd6V_3g`)
3. `-db` or `--save-to-db`. Shows that you want load processed data into DataBase. You must create (or ask) for a `.env` file with DB config. And put it in the main directory
4. `-all` or `--save-to-all`. Shows that you want load processed data into defaut `.parquet`-file and into DataBase. As `-db` requires `.env`-file with DB config

---

### Starting code
Before you start the code **I strongly recommend** you read the [cli-arguments part](#cli-arguments)  
To start code write:  
```cmd
python etl/main.py
```  
By default, code uses `data/raw/gaschromatography.csv` and saves data into `.parquet`-file in `data/processed/` directory

---

### EDA render
Render (without plotly graphs visualisation) EDA.ipynb [link](https://nbviewer.org/github/Eternal-insomnia/DDE-repo/blob/main/notebooks/EDA.ipynb)
