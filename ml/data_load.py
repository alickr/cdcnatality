import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
import os

def fetchCollumns(columns_list, extra_query=''):
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user=os.getenv("DB_USER"),
                                   pw=os.getenv("DB_PASSWORD"),
                                   db=os.getenv("DB_DATABASE")))

    cols = ', '.join(columns_list)
    if type(os.getenv("DB_TABLE")) != 'NoneType' :
        database_table = os.getenv("DB_TABLE") 
    else:
        database_table = "all_years_proper_template"

    # %time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_SURF,AB_ANTI,AB_SEIZ,F_AB_VENT,F_AB_VENT6,F_AB_NIUC,F_AB_SURFAC,F_AB_ANTIBIO,F_AB_SEIZ,NO_ABNORM,AB_NICU FROM all_years_data;', engine)

    df = pd.read_sql_query('SELECT ' + cols + ' FROM '+ os.getenv("DB_DATABASE") + '.' + database_table +' '+ extra_query, engine)

    return df

# df.head()
# df.shape

# --- Preparing Data For Training ---
# y = dataset.iloc[:, 4].values
# X = dataset.iloc[:, 0:4].values
# df.isnull().any()

# %time label_encoding(df)

# %time df.corr(method ='pearson')

# x = df.loc[:, ~df.columns.isin(['AB_NICU','DOB_YY'])] # Remove Specific column by name
# y = df.AB_NICU.values
