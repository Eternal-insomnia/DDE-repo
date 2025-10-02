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

country_status = []
country_capital = []
country_region = []
country_subregion = []
country_area = []
country_population = []

for country in tqdm(country_names):
    response = make_request(f'/name/{country}')[0]
    country_status.append(response.get('status'))
    country_capital.append(response.get('capital'))
    country_region.append(response.get('region')[0])
    country_subregion.append(response.get('subregion'))
    country_area.append(response.get('area'))
    country_population.append(response.get('population'))

df = pd.DataFrame(data={'Name': country_names, 
                        'Status': country_status, 
                        'Capital': country_capital, 
                        'Region': country_region, 
                        'Subregion': country_subregion,
                        'Area': country_area,
                        'Population': country_population})

print(df.head())