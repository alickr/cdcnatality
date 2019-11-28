import dask.dataframe as dd
df = dd.read_csv('./csv/Nat2018us.csv')
df.head()
print(df.shape[1])
df.isnull().sum()