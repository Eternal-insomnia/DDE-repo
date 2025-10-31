import pandas as pd

# Transforming data
def data_processing(data: pd.DataFrame) -> pd.DataFrame:
    data["Retention index type"] = data["Retention index type"].astype("category")
    data["Is column polar"] = data["Column polarity"].map({"polar column": True, "non-polar column": False})
    data = data.drop("Column polarity", axis=1)
    data["Carrier gas"] = data["Carrier gas"].replace("He", "Helium")
    data["Carrier gas"] = data["Carrier gas"].replace("N2", "Nitrogen")
    data["Carrier gas"] = data["Carrier gas"].replace("H2", "Hydrogen")
    data["Carrier gas"] = data["Carrier gas"].replace("N2/He", "He or N2")
    data["Carrier gas"] = data["Carrier gas"].astype("category")
    data["Temperature regime"] = data["Temperature regime"].astype("category")
    data["I"] = data["I"].astype("float32")
    data["Temperature"] = data["Temperature"].drop(data[data["Temperature"] == "40. to 190."].index)
    data["Temperature"] = data["Temperature"].astype("float32")
    data["Tstart"] = data["Tstart"].astype("float32")
    data["Tend"] = data["Tend"].astype("float32")
    data["Heat rate"] = data["Heat rate"].astype("float32")
    data["Initial hold"] = data["Initial hold"].astype("float32")
    data["Final hold"] = data["Final hold"].astype("float32")
    data["Column type"] = data["Column type"].astype("category")
    data["Column length"] = data["Column length"].astype("float32")
    data["Column diameter"] = data["Column diameter"].astype("float32")
    data["Phase thickness"] = data["Phase thickness"].astype("float32")
    return data