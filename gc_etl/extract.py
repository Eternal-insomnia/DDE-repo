import pandas as pd


# Reading data
def read_dataset(data_path: str) -> pd.DataFrame:
    df = pd.read_csv(data_path, sep=";")
    print("Data extracted")
    print(df.head(10))
    return df
