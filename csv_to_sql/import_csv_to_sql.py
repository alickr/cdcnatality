import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sqlalchemy import create_engine
from importlib import reload
import reduce_columns_module as column_reducer

reload(column_reducer)

file_lists = [
    # 'abnormal_conditions_of_the_newborn',
    # 'apgar',
    # 'characteristics_of_labor_and_delivery',
    'child',
    # 'congenital_anomalies_of_the_newborn',
    # 'data_analysed_from_history',
    # 'delivery_attendant',
    # 'father',
    # 'infection_present',
    # 'maternal_morbidity',
    # 'method_of_delivery',
    # 'mother',
    # 'mother_height_weight',
    # 'obstetric_procedures',
    # 'precare',
    # 'risk_factor',
    # 'sex_record',
    # 'wic'
]

year = 2014

for item in file_lists:
    # if( item == 'data_analysed_from_history' ):
    #     continue
    df = pd.read_csv('data/' + str(year) + '_' + item + ".csv")
    df.drop(['Unnamed: 0'], axis=1, errors='ignore', inplace=True)

    temp_start = 15611134
    #7666289 for 2016
    #11622401 for 2015
    #15611134 for 2014

    df['id'] = [i for i in range(temp_start, df.shape[0] + temp_start )]
    # df['child_id'] = df['id']
    df.to_csv('data/' + str(year) + '_' + item + ".csv")

    # column_reducer.store_to_sql(df, item)
    # df.head(5)
    # df.columns

for index, row in df.iterrows():
    temp = list(row)

    break

temp1 = pd.read_csv('data/2015_risk_factor.csv')

temp2 = pd.read_csv('data/2016_child.csv')
temp3 = pd.read_csv('data/2015_child.csv')
temp4 = pd.read_csv('data/2017_child.csv')
temp5 = pd.read_csv('data/2015_child.csv')
temp6 = pd.read_csv('data/2015_apgar.csv')


