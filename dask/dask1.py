import dask.dataframe as dd
import pandas as pd
import copy

df = dd.read_csv('./csv/Nat2018us.csv')
df_pd = pd.read_csv('./csv/Nat2018us.csv')

df_pd.head()
df_pd.describe()
df_pd.isnull().sum()

df = df[["CA_ANEN",
    "CA_MNSB",
    "CA_CCHD",
    "CA_CDH",
    "CA_OMPH",
    # "CA_GAST",
    # "F_CA_ANEN",
    # "F_CA_MENIN",
    # "F_CA_HEART",
    # "F_CA_HERNIA",
    # "F_CA_OMPHA",
    "F_CA_GASTRO",
    "CA_LIMB",
    "CA_CLEFT",
    # "CA_CLP_AL",
    # "CA_DOWN",
    # "CA_DISOR",
    # "CA_HYPO",
    # "F_CA_LIMB",
    # "F_CA_CLEFTLP",
    # "F_CA_CLEFT",
    # "F_CA_DOWNS",
    # "F_CA_CHROM",
    "F_CA_HYPOS",
    "NO_CONGEN"]]

df_copy = copy.deepcopy(df[["F_CA_HYPOS","NO_CONGEN"]])
df_copy.head().describe()
df_copys.describe()

df.head()
print(df.shape)
df.isnull().sum().show()

s = df.isnull().sum()
s
for x in df_copy.isnull().sum():
    print(x)


