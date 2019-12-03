%%time
from sqlalchemy import create_engine
import pandas as pd
# Create a sql engine that connects to AWS RDS
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))
                               
# Load all the reviews
# %time df_ab = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_NICU FROM all_years_data;', engine)
%time df_ab = pd.read_sql_query('SELECT * FROM abnormal_conditions_of_the_newborn;', engine)

# Drop duplicates
# df_ab = df_ab.drop_duplicates()

df_ab.shape
df_ab.AB_NICU.isnull().sum()
df_ab.corr(method ='kendall')
%time df_ab.corr(method ='pearson')

