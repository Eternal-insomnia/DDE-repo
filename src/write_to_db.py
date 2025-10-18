from sqlalchemy import create_engine, text, inspect
import sqlite3
import os
import pandas as pd

script_path = os.path.dirname(os.path.abspath(__file__))

creds_path = script_path + "\\creds.db"
conn = sqlite3.connect(creds_path)
cur = conn.cursor()

# get access parameters
cur.execute("SELECT * FROM access LIMIT 1;")
row = [r for r in cur.fetchall()]
cur.execute("PRAGMA table_info(access)")
cols = [r for r in cur.fetchall()]
conn.close()

# create dict with access parameters
for i in range(len(cols)):
    cols[i] = list(cols[i])
cols_transpose = [list(row) for row in zip(*cols)]
data = dict(zip(cols_transpose[1], row[0]))

db_user = data['user']
db_password = data['pass']
db_url = data['url']
db_port = data['port']
db_root_base = 'homeworks'

df = pd.read_parquet(os.path.dirname(script_path) + "\\data\\gas_chromatography.parquet")
df = df[:100]

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
    pool_recycle=3600,
    echo=True,
)

df.to_sql(
    name="suvorov",
    con=engine,
    schema="public",
    if_exists="replace",  # или "append"
    index=True,
)

with engine.begin() as conn:
    rows = conn.execute(text('ALTER TABLE public.suvorov ADD PRIMARY KEY (index)'))

inspector = inspect(engine)
columns = inspector.get_columns("suvorov", schema="public")

print({col["name"]: col["type"] for col in columns})

# with engine.begin() as conn:
#     query = """
#     SELECT *
#     FROM public.suvorov
#     LIMIT 10
#     """
#     rows = conn.execute(text(query)).all()
