import requests
# import pandas as pd

API_URL = "https://restcountries.com/v3.1"

items = []
response = requests.get(
    API_URL + "/all?fields=name", 
    headers={"Content-Type": "application/json"},
)
if response.status_code == 200:
    items = response.json()
    print(items)
else:
    msg = f"Response code is {response.status_code}"
    raise Exception(msg)