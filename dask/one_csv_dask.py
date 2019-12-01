import dask.dataframe as dd
import pandas as pd
import copy
import gc

# df2018.head()
# df2018.describe()
# df2018.isnull().sum()

# data_frames = [df1, df2, df3]

# merge csv files and manually garbage collect
df2017 = dd.read_csv('./csv/Nat2017us.csv',dtype={'DMAR': 'object'})
df2018 = dd.read_csv('./csv/Nat2018us.csv',dtype={'DMAR': 'object'})
all_df = dd.concat([df2018,df2017], axis=0, ignore_index=True, sort=False)
del [[df2017,df2018]]
gc.collect()

df2016 = pd.read_csv('./csv/Nat2016us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2016], axis=0, ignore_index=True, sort=False)
del [[df2016]]
gc.collect()

df2015 = pd.read_csv('./csv/Nat2015us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2015], axis=0, ignore_index=True, sort=False)
del [[df2015]]
gc.collect()

df2014 = pd.read_csv('./csv/Nat2014us.csv',dtype={'DMAR': 'object'})
%time all_df = pd.concat([all_df,df2014], axis=0, ignore_index=True, sort=False)
del [[df2014]]
gc.collect()

print("DONE!")

all_df.head()
all_df.shape

# all_df.DOB_YY.unique()
# all_df.isnull().sum()

%time all_df.to_csv('./csv/all_years.csv', mode='a', header=False) # To CSV

## Send To MySql
# from sqlalchemy import create_engine
## import pmysql

# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                        .format(user="dev",
#                                pw="rooting",
#                                db="cdcnatality"))

# all_df.to_sql(con=engine, name='all_years_template', if_exists='append') # Code To Save Into Mysql/Mariadb Database
