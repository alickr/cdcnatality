import dask.dataframe as dd
import pandas as pd
import copy
import gc

# df2018.head()
# df2018.describe()
# df2018.isnull().sum()

# data_frames = [df1, df2, df3]

# merge csv files and manually garbage collect
df2017 = pd.read_csv('./csv/Nat2017us.csv',dtype={'DMAR': 'object'})
df2018 = pd.read_csv('./csv/Nat2018us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([df2018,df2017], axis=0, ignore_index=True, sort=False)
del [[df2017,df2018]]
gc.collect()
print("step 1!")

df2016 = pd.read_csv('./csv/Nat2016us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2016], axis=0, ignore_index=True, sort=False)
del [[df2016]]
gc.collect()
print("step 2!")

df2015 = pd.read_csv('./csv/Nat2015us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2015], axis=0, ignore_index=True, sort=False)
del [[df2015]]
gc.collect()
print("step 3!")

df2014 = pd.read_csv('./csv/Nat2014us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2014], axis=0, ignore_index=True, sort=False)
del [[df2014]]
gc.collect()

print("DONE CONCAT!")

# all_df.head()
all_df.shape

# all_df.DOB_YY.unique()
# all_df.isnull().sum()

all_df.to_csv('./csv/all_years_combined.csv', mode='a', header=False) # To CSV
# del [[all_df]]
# gc.collect()
print("DONE SAVING CSV!")

# df_chunk = pd.read_fwf(r'./data/Nat2018us/Nat2018PublicUS.c20190509.r20190717.txt', chunksize=1000000,colspecs=list_colspecs, header=None )
# # Each chunk is in df format
# for chunk in df_chunk:
#     chunk.to_csv('./csv/all_chunks.csv', mode='a', header=False, index=False)

from sqlalchemy import create_engine
# # import pmysql

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))

all_df.to_sql(con=engine, name='all_years_combined', if_exists='append') # Code To Save Into Mysql/Mariadb Database
