# %reset
%%time
import numpy as np
import pandas as pd
import copy

# --- Importing Dataset ---
# Create a sql engine that connects to AWS RDS
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))
                               
# %time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_NICU FROM all_years_data;', engine)
# %time df = pd.read_sql_query('SELECT * FROM abnormal_conditions_of_the_newborn;', engine)
%time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6, MM_MTR,MM_PLAC,MM_RUPT,MM_UHYST,MM_AICU,AB_NICU  FROM all_years_proper_template;', engine)
# %time df = pd.read_sql_query('SELECT * FROM all_years_proper_template;', engine)
df
# --- Preparing Data For Training ---
# y = dataset.iloc[:, 4].values
# X = dataset.iloc[:, 0:4].values
df.isnull()


# BEGIN ENCODING
df_encode = df
# Categorical boolean mask
categorical_feature_mask = df_encode.dtypes==object
# filter categorical columns using mask and turn it into a list
categorical_cols = df_encode.columns[categorical_feature_mask].tolist()

# import labelencoder
from sklearn.preprocessing import LabelEncoder
# instantiate labelencoder object
le = LabelEncoder()

# apply le on categorical feature columns
df_encode[categorical_cols] = df_encode[categorical_cols].apply(lambda col: le.fit_transform(col))
df_encode[categorical_cols].head(10)
df_encode
df
# STOP ENCODING

%time df.corr(method ='pearson')

X = df.loc[:, ~df.columns.isin(['AB_NICU','DOB_YY'])] # Remove Specific column by name
y = df.AB_NICU.values
y
# df.MM_MTR.unique()


# Random Forests
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, y_test = train_test_split(X, y,random_state=0)

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(n_estimators=100,oob_score=True) #max_features=5

random_forest.fit(X_train, Y_train)

Y_pred = random_forest.predict(X_test)

random_forest.score(X_train, Y_train)
random_forest.get_params,random_forest.feature_importances_

Y_pred


