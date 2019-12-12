import random

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
import os


def fetchCollumns(columns_list, extra_query=''):
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=os.getenv("DB_USER"),
                                   pw=os.getenv("DB_PASSWORD"),
                                   db=os.getenv("DB_DATABASE")))

    cols = ', '.join(columns_list)
    if type(os.getenv("DB_TABLE")) != 'NoneType':
        database_table = os.getenv("DB_TABLE")
    else:
        database_table = "all_years_proper_template"

    # %time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_SURF,AB_ANTI,AB_SEIZ,F_AB_VENT,F_AB_VENT6,F_AB_NIUC,F_AB_SURFAC,F_AB_ANTIBIO,F_AB_SEIZ,NO_ABNORM,AB_NICU FROM all_years_data;', engine)

    df = pd.read_sql_query(
        'SELECT ' + cols + ' FROM ' + os.getenv("DB_DATABASE") + '.' + database_table + ' ' + extra_query, engine)

    return df


def fetch_rand_data(columns_list, rows_per_year=1000):
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=os.getenv("DB_USER"),
                                   pw=os.getenv("DB_PASSWORD"),
                                   db=os.getenv("DB_DATABASE")))

    chunk_head = pd.read_sql_query(
        'SELECT MAX(id) as id_max,  MIN(id) as id_min, DOB_YY FROM all_years_data GROUP BY DOB_YY', engine)

    final = pd.DataFrame()
    cols = ', '.join(columns_list)
    if type(os.getenv("DB_TABLE")) != 'NoneType':
        database_table = os.getenv("DB_TABLE")
    else:
        database_table = "all_years_proper_template"

    li = []
    for index, row in chunk_head.iterrows():
        li.extend([random.randint(row['id_min'], row['id_max']) for i in range(rows_per_year + 1)])

    li.sort()
    m = len(li)
    limit = 1000
    temp1 = range(limit, m + 1, limit)
    temp2 = 0
    for temp3 in temp1:
        id_list = li[temp2: temp3]
        id_list = ','.join(str(x) for x in id_list)

        if (temp2 == 0):
            final = pd.read_sql_query('SELECT ' + cols + ' FROM ' + os.getenv("DB_DATABASE") + '.' + database_table +
                                      ' WHERE id IN (' + id_list + ')', engine)
        else:
            chunk = pd.read_sql_query('SELECT ' + cols + ' FROM ' + os.getenv("DB_DATABASE") + '.' + database_table +
                                      ' WHERE id IN (' + id_list + ')', engine)

            final = pd.concat([final, chunk])

        temp2 = temp3

    return final
