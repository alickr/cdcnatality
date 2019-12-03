import time
start = time.time()

import dask.dataframe as dd
import pandas as pd
import copy
import gc

# df2018.head()
# df2018.describe()
# df2018.isnull().sum()

# data_frames = [df1, df2, df3]

# merge csv files and manually garbage collect
print("step 1/4!")
df2017 = pd.read_csv('./csv/Nat2017us.csv',dtype={'DMAR': 'object'})
df2018 = pd.read_csv('./csv/Nat2018us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([df2018,df2017], axis=0, ignore_index=True, sort=False)
del [[df2017,df2018]]
gc.collect()
print ('Execution Time: ', (time.time()- start)/60 ,' minutes')
print("step 2/4!")

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

df2016 = pd.read_csv('./csv/Nat2016us_v2.csv',dtype={'DMAR': 'object'},index_col=False)
# df2016.head(10)
all_df = pd.concat([all_df,df2016], axis=0, ignore_index=True, sort=False)
del [[df2016]]
gc.collect()
print ('Execution Time: ', (time.time()- start)/60 ,' minutes')
print("step 3/4!")

df2015 = pd.read_csv('./csv/Nat2015us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2015], axis=0, ignore_index=True, sort=False)
del [[df2015]]
gc.collect()
print ('Execution Time: ', (time.time()- start)/60 ,' minutes')
print("step 4/4!")

df2014 = pd.read_csv('./csv/Nat2014us.csv',dtype={'DMAR': 'object'})
all_df = pd.concat([all_df,df2014], axis=0, ignore_index=True, sort=False)
# del [[all_df]]
# gc.collect()
print ('Execution Time: ', (time.time()- start)/60 ,' minutes')
print("SAVING CSV file!")

# all_df.head()
# all_df.shape

# all_df.DOB_YY.unique()
# all_df.isnull().sum()

all_df.to_csv('./csv/all_years_proper.csv', mode='a', header=False) # To CSV
print("DONE SAVING CSV!")


# from sqlalchemy import create_engine
# # import pmysql

# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                        .format(user="dev",
#                                pw="rooting",
#                                db="cdcnatality"))

# all_df.to_sql(con=engine, name='all_years_template', if_exists='append') # Code To Save Into Mysql/Mariadb Database

print("DONE. SUCCESSFULLY COMPLETED ALL TASKS!")
print ('Overall Execution Time: ', (time.time()- start)/60 ,' minutes')