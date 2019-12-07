from sklearn.model_selection import GridSearchCV
import ml.data_load as data_load
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import ml.modeling as modeling

cols1 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

cols2 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

# df = data_load.fetchCollumns(cols1, extra_query='') #extra_query='LIMIT 100'
df = data_load.fetchCollumns(cols1, extra_query='LIMIT 100') #extra_query='LIMIT 100'

# df.isnull().sum()
df = df[df.AB_NICU != "U"] #Drop Column with U Unknown 
df = df[df.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan

%time modeling.label_encoding(df) #If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values

test_size=0.33
random_state=0
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=0)
rfc=RandomForestClassifier(random_state=0)


param_grid = { 
    'n_estimators': [1,2,3,5,10,20,50,100,200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [1,2,3,4,5,6,7,8,9,10],
    'criterion' :['gini', 'entropy']
}

%time CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5, n_jobs=-1)
CV_rfc.fit(x_train, y_train)

CV_rfc.best_params_

# Random Forests
def gridSearch_random_forest(x, y, test_size_val=0.33, random_state_val=0, **params):
    param_grid = { 
        'n_estimators': [1,2,3,5,10,20,50,100,200, 500],
        'max_features': ['auto', 'sqrt', 'log2'],
        'max_depth' : [1,2,3,4,5,6,7,8,9,10],
        'criterion' :['gini', 'entropy']
    }

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)

    model = RandomForestClassifier(n_estimators=100, oob_score=True, **params)  # max_features=5
    model.fit(x_train, y_train)

    %time CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5, n_jobs=-1)
    CV_rfc.fit(x_train, y_train)

    CV_rfc.best_params_

    return model, x_train, x_test, y_train, y_test


# Support Vector Machine
def gridSearch_support_vector_machine(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = SVC(**params)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

# xgb_classifier
def gridSearch_xgb_classifier(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = XGBClassifier(**params)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test