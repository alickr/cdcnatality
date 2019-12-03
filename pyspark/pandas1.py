import pandas as pd

column_names = [
    'age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital-gain',
    'capital-loss',
    'hours-per-week',
    'native-country',
    'salary'
]

train_df = pd.read_csv('./pyspark/adult.data', names=column_names)
test_df = pd.read_csv('./pyspark/adult.test', names=column_names)

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path
cwd = os.getcwd()
cwd

train_df = train_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
train_df_cp = train_df.copy()
train_df_cp = train_df_cp.loc[train_df_cp['native-country'] != 'Holand-Netherlands']
train_df_cp.to_csv('./pyspark/train.csv', index=False, header=False)
test_df = test_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
test_df.to_csv('./pyspark/test.csv', index=False, header=False)

print('Training data shape: ', train_df.shape)
train_df.head()