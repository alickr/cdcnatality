import time
start = time.time()

import pandas as pd
import sqlalchemy as sql
from sqlalchemy import create_engine
# import pmysql

sql_engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))

# connect_string = 'mysql://USER:PW@DBHOST/DB'

# sql_engine = sql.create_engine(connect_string)

query = "SELECT * FROM cdcnatality.tbl_cdc LIMIT 500;"
# query = "SELECT * FROM cdcnatality.tbl_cdc;"


df = pd.read_sql_query(query, sql_engine)
print(df.describe())

for chunk in pd.read_sql_query(query , sql_engine, chunksize=5):
    print(type(chunk))
    chunk.describe()

print("Done!")
print ('Execution Time: ', time.time()- start ,' Seconds')