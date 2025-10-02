import requests
from tqdm import tqdm
import pandas as pd

API_URL = "https://restcountries.com/v3.1"

def make_request(url_tail):
    response = requests.get(
        API_URL + url_tail, 
        headers={"Content-Type": "application/json"},
    )
    if response.status_code == 200:
        return response.json()
    else:
        msg = f"Response code is {response.status_code}"
        raise Exception(msg)

countries = make_request('/all?fields=name')
country_names = []

for country in countries:
    country_names.append(country.get('name')['common'])

df = pd.DataFrame(columns=['Название', 'Столица', 'Население', 'Площадь', 'Континент', 'Регион', 'Признанность'])

for country in tqdm(country_names):
    response = make_request(f'/name/{country}')[0]
    if response.get('capital'):
        df.loc[len(df)] = [country, response.get('capital')[0], response.get('population'), response.get('area'), response.get('region'), response.get('subregion'), response.get('status')]

print(df.head(10))

df.to_csv('countries.csv', index=False)