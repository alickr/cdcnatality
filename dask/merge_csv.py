import dask.dataframe as dd
import pandas as pd
import copy
pd.set_option('display.max_colwidth', -1)

# df = dd.read_csv('./csv/Nat2018us.csv')
# df_pd = pd.read_csv('./csv/Nat2018us.csv')
# %time
df2014 = dd.read_csv('./csv/Nat2014us.csv',dtype={'DMAR': 'object'})
df2015 = dd.read_csv('./csv/Nat2015us.csv',dtype={'DMAR': 'object'})
df2017 = dd.read_csv('./csv/Nat2017us.csv',dtype={'DMAR': 'object'})
df2018 = dd.read_csv('./csv/Nat2018us.csv',dtype={'DMAR': 'object'})

# pd_df2014 = pd.read_csv('./csv/Nat2014us.csv',dtype={'DMAR': 'object'})
# pd_df2015 = pd.read_csv('./csv/Nat2015us.csv',dtype={'DMAR': 'object'})
# pd_df2017 = pd.read_csv('./csv/Nat2017us.csv',dtype={'DMAR': 'object'})
# pd_df2018 = pd.read_csv('./csv/Nat2018us.csv',dtype={'DMAR': 'object'})

df2018[["MAGER14"]]

x = df2018.describe()

# x.persist()

# df2018.persist()
# df2018.describe()

df2018.MAGER14.Value_counts().compute()


