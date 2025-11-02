import pandas as pd


# Transforming data
def data_processing(data: pd.DataFrame) -> pd.DataFrame:
    # DTypes dict
    data_types = {
        "Compound ID": "object",
        "Compound name": "object",
        "InChI": "object",
        "Retention index type": "category",
        "Active phase": "object",
        "Carrier gas": "category",
        "Temperature regime": "category",
        "I": "float32",
        "Temperature": "float32",
        "Tstart": "float32",
        "Tend": "float32",
        "Heat rate": "float32",
        "Initial hold": "float32",
        "Final hold": "float32",
        "Program": "object",
        "Column type": "category",
        "Column length": "float32",
        "Column diameter": "float32",
        "Phase thickness": "float32",
        "Substrate": "object",
        "Reference": "object",
        "Comment": "object",
        "Is column polar": "boolean",
    }

    data["Is column polar"] = data["Column polarity"].map(
        {"polar column": True, "non-polar column": False}
    )
    data = data.drop("Column polarity", axis=1)

    data["Carrier gas"] = data["Carrier gas"].replace("He", "Helium")
    data["Carrier gas"] = data["Carrier gas"].replace("N2", "Nitrogen")
    data["Carrier gas"] = data["Carrier gas"].replace("H2", "Hydrogen")
    data["Carrier gas"] = data["Carrier gas"].replace("N2/He", "He or N2")

    data["Temperature"] = data["Temperature"].drop(
        data[data["Temperature"] == "40. to 190."].index
    )

    # Converting into correct dtypes
    data = data.astype(data_types)

    return data
