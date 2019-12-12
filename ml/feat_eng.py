import pandas as pd
pd.set_option('display.max_columns', 100)

#load csv
# df = pd.read_csv("../analysis/results_dec.csv", sep='\t')

#imputation
def impute(df):
    if 'AB_NICU' in df.columns:
        df = df[df.AB_NICU != "U"] #Drop Column with U Unknown
        df = df[df.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan
        
    impute_u = ["RF_PDIAB", "RF_GDIAB", "RF_PHYPE", "RF_GHYPE", "RF_EHYPE", "RF_PPTERM", "RF_INFTR","RF_FEDRG", "RF_ARTEC",
    "RF_CESAR","NO_RISKS", "IP_GON", "IP_SYPH", "IP_CHLAM", "IP_HEPB", "IP_HEPC", "NO_INFEC", "CIG_REC", "WIC", "AB_NICU" ]
    for item in impute_u:
        if item in df.columns:
            df[item].fillna("U", inplace=True)   
    
    if 'MRACE31' in df.columns:
        # many values belongs to first category : White race
        df["MRACE31"].fillna(df['MRACE31'].median(), inplace=True)
        
    impute_9 = ["FRACE6", "FEDUC", "MEDUC", "DMAR", "NO_MMORB"]
    for item in impute_9:
        if item in df.columns:
            df[item].fillna(9, inplace=True)
        
    impute_99 = ["ILLB_R11","ILP_R11", "PRECARE", "M_Ht_In","BMI"]
    for item in impute_99:
        if item in df.columns:
            df[item].fillna(99, inplace=True)
        
    impute_6 = ["CIG0_R","CIG1_R","CIG2_R", "CIG3_R"]
    for item in impute_6:
        if item in df.columns:
            df[item].fillna(6, inplace=True)

    df = df[df.AB_NICU != "U"] #Drop Column with U Unknown
    df = df[df.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan
    # df = df[df.CIG0_R != 6] #Drop Column with U Unknown
    df = df[df.NO_INFEC != 9] #Drop Column with U Unknown
    df = df[df.NO_MMORB != 9] #Drop Column with U Unknown
    df = df[df.NO_RISKS != 9] #Drop Column with U Unknown

    df = df[df.BMI != 99] #Drop Column with U Unknown
    df = df[df.PRECARE != 99] #Drop Column with U Unknown

    return df

#find correlation

def filterColumns(df):
    df_corr = df.corr()
    
    # get positive values only
    df_corr = df_corr[df_corr['AB_NICU'] > 0]
    
    # find mean for the predicted value
    avg = (df_corr['AB_NICU']).mean(axis=0)
    
    # filter the values only greater than mean
    df_final = df_corr[df_corr['AB_NICU'] > avg]
    
    # reduce number of columns
    df_final = df_final[['RF_PDIAB','RF_PHYPE','RF_GHYPE','RF_EHYPE','RF_PPTERM','RF_INFTR','RF_FEDRG','AB_NICU']]

    return df_final

def feature_engineering(df):
    df = impute(df)
    # df = filterColumns(df)
    # df = df[df.AB_NICU != "U"] #Drop Column with U Unknown
    # df = df[df.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan
    return df



# print(df.head(10))