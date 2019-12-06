import pandas as pd
pd.set_option('display.max_columns', 100)

#load csv
df = pd.read_csv("results_dec.csv", sep='\t')

# delete AB_NICU na columns


df['AB_NICU'].dropna()

#imputation
# unknown or not stated
impute_u = ["RF_PDIAB", "RF_GDIAB", "RF_PHYPE", "RF_GHYPE", "RF_EHYPE", "RF_PPTERM", "RF_INFTR","RF_FEDRG", "RF_ARTEC",
 "RF_CESAR","NO_RISKS", "IP_GON", "IP_SYPH", "IP_CHLAM", "IP_HEPB", "IP_HEPC", "NO_INFEC", "CIG_REC", "WIC" ]

for item in impute_u:
    df[item].fillna("U", inplace=True)    


# many values belongs to first category : White race
df["MRACE31"].fillna(df['MRACE31'].median(), inplace=True)


impute_9 = ["FRACE6", "FEDUC", "MEDUC", "DMAR", "NO_MMORB"]
for item in impute_9:
    df[item].fillna(9, inplace=True)

impute_99 = ["ILLB_R11","ILP_R11", "PRECARE", "M_Ht_In","BMI"]
for item in impute_99:
    df[item].fillna(99, inplace=True)

impute_6 = ["CIG0_R","CIG1_R","CIG2_R", "CIG3_R"]
for item in impute_6:
    df[item].fillna(6, inplace=True)



#function to parse
def parseToInt(val):
    if(val == 'X'):
        return 0
    elif(val == 'U'):
        return 1
    elif(val == 'N'):
        return 2
    elif(val == 'Y'):
        return 3
    else:
        return 4


# parse the columns

cols_to_parse = ['WIC', 'CIG_REC', 'RF_PDIAB', 'RF_GDIAB', 'RF_PHYPE', 'RF_GHYPE', 'RF_EHYPE', 'RF_PPTERM', 'RF_INFTR', 'RF_FEDRG',
'RF_ARTEC', 'RF_CESAR', 'NO_RISKS', 'IP_GON','IP_SYPH', 'IP_CHLAM', 'IP_HEPB', 'IP_HEPC', 'NO_INFEC', 'AB_NICU'   ]

for item in cols_to_parse:
    df[item] = pd.DataFrame(list(map(parseToInt, df[item])))


#find correlation

df_corr = df.corr()

# get positive values only
df_corr = df_corr[df_corr['AB_NICU'] > 0]

# find mean for the predicted value
avg = (df_corr['AB_NICU']).mean(axis=0)

# filter the values only greater than mean
df_final = df_corr[df_corr['AB_NICU'] > avg]

# reduce number of columns
df_final = df_final[['RF_PDIAB','RF_PHYPE','RF_GHYPE','RF_EHYPE','RF_PPTERM','RF_INFTR','RF_FEDRG','AB_NICU']]

# view the df
df_final