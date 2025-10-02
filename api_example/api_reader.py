import requests
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

print(country_names)

country_status = []

for country in country_names:
    country_status.append(make_request(f'/name/{country}')[0].get('status'))

print(country_status)