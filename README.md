# DDE-repo
Created for ITMO's Data Driven Engineering homework

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
4. Install dependencies: ```conda env create -f environment.yml```

---

### CLI-argumets
This project has a few CLI-arguments:  
1. `-ext-l` or `--extract-local` with CSV-file name (e.g. `-ext-l test.csv`). Create `data/raw` folder in the project directory. Move .csv file into `data/raw` folder
2. `-ext-g` or `--extract-gdrive` with CSV-file Google Drive id (e.g. `-ext-g 123`)
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

### Repository structure
```

DDE-repo/
│
├── cache/                          # Pictures from README
│
├── etl/                            # Extract, Transform, Load process
|   ├── __init__
|   ├── extract.py                  # Data extract (from local or GDrive)
|   ├── transform.py                # Data typing, cleaning
|   ├── load.py                     # Data load (to local or DB or both)
|   ├── main.py                     # Main module (orchestrator)
|
├── experiments/                    # Some experiments
│   ├── api_reader.py               # Parsing API script
│   └── README.md                   # Parsing documentation
│
├── notebooks/                       
│   ├── dtypes.ipynb                # Dataset research for matching dtypes
|   └── EDA.ipynb                   # Exploratory Data Analysis
|
├── .gitignore
├── environment.yml                 # Conda environment config
└── README.md                       # Project documentation

```

---

### EDA render
Render (without plotly graphs visualisation) EDA.ipynb [link](https://nbviewer.org/github/Eternal-insomnia/DDE-repo/blob/main/notebooks/EDA.ipynb)
