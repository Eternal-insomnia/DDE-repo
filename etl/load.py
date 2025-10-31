import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Saving data into parquet file
def save_to_parquet(data: pd.DataFrame):
    data.to_parquet("data/gas_chromatography.parquet", index = False)
    print("Data saved to parquet!")

# Saving data into DB
def save_to_db(data: pd.DataFrame):
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASS")
    db_url = os.getenv("DB_URL")
    db_port = os.getenv("DB_PORT")
    db_root_base = os.getenv("DB_ROOT_BASE")

    df = data[:100]

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
        pool_recycle=3600,
        echo=True,
    )

    db_table_name = "suvorov"
    if os.getenv("DB_TABLE_NAME") is not None:
        db_table_name = os.getenv("DB_TABLE_NAME")

    df.to_sql(
        name=db_table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=True,
    )

    with engine.begin() as conn:
        _ = conn.execute(text(f"ALTER TABLE public.{db_table_name} ADD PRIMARY KEY (index)"))
    
    print("Data saved to DB!")