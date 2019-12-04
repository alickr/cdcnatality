import copy
import pandas as pd

# --- Importing Dataset ---
# Create a sql engine that connects to AWS RDS
from sqlalchemy import create_engine


def fetchCollumns(columns_list):
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                           .format(user="dev",
                                   pw="rooting",
                                   db="cdcnatality"))

    cols = ', '.join(columns_list)
    # %time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_SURF,AB_ANTI,AB_SEIZ,F_AB_VENT,F_AB_VENT6,F_AB_NIUC,F_AB_SURFAC,F_AB_ANTIBIO,F_AB_SEIZ,NO_ABNORM,AB_NICU FROM all_years_data;', engine)
    df = pd.read_sql_query('SELECT ' + cols + ' FROM all_years_proper_template;', engine)

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
