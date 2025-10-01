import requests
import pandas as pd

API_URL = "https://restcountries.com/v3.1"

countries = []
response = requests.get(
    API_URL + "/all?fields=name", 
    headers={"Content-Type": "application/json"},
)
if response.status_code == 200:
    countries = response.json()
else:
    msg = f"Response code is {response.status_code}"
    raise Exception(msg)

country_names = []

for country in countries:
    country_names.append(country.get('name')['common'])

print(country_names)

df = pd.DataFrame(countries)