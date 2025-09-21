import pandas as pd

# Reading data
def read_dataset(url):
    df=pd.read_csv(url, sep=';', encoding='latin-1')
    print(df.head(10))
    return df

url = 'https://drive.google.com/uc?id=14jdCxjCsB0NT5ExKhWByxMiNHvd6V_3g'
df = read_dataset(url)