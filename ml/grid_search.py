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
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier

import numpy as np
from sklearn import datasets  # sample dataset
import ml.modeling as modeling
from ml.selected_columns import selected_columns,cols_feat # Columns to Select From SQL Database
from ml.feat_eng import impute # Feature Engineering
# %matplotlib inline

# selected_columns
%time df = data_load.fetch_rand_data(selected_columns,rows_per_year=2000) #pull random 2000 rec per year
# df = df_full[df_full.DOB_YY != 2018]
# df_test = df_full[df_full.DOB_YY == 2018]
# df = df_full
# Perform Feature Engineering and Imputaions
df
df = df[df.AB_NICU != "U"] #Drop Column with U Unknown
df.NO_RISKS.unique()
df.NO_INFEC.unique()
df.NO_MMORB.unique()

# NO_RISKS

# df = df[df.NO_RISKS != 9] #Drop Column with U Unknown
# df = df[df.NO_INFEC != 9] #Drop Column with U Unknown
# df = df[df.NO_MMORB != 9] #Drop Column with U Unknown

# df.shape
df = impute(df)
modeling.label_encoding(df) #If Data is not encoded

x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values

# Random Forests
def gridSearch_random_forest(x, y, param_grid):
    # param_grid = { 
    #     'n_estimators': [2,5,10,20,50,100, 200,300,400,500,600],
    #     'max_features': ['auto', 'sqrt', 'log2',1,5,10,20],
    #     'max_depth' : [1,5,10,50,100],
    #     'criterion' :['gini', 'entropy'],
    #     'class_weight': [{0:15,1:1},{0:10,1:1},'balanced',{0:1,1:10}],
    #     'n_jobs':[-1],
    # }

    rfc = RandomForestClassifier()  # max_features=5

    CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5, n_jobs=-1)
    CV_rfc.fit(x, y)

    CV_rfc.best_params_

    return CV_rfc.best_params_

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

def dtree_random_forest(x, y, param_grid):
    # param_grid = { 
    #     'n_estimators': [2,5,10,20,50,100, 200,300,400,500,600],
    #     'max_features': ['auto', 'sqrt', 'log2',1,5,10,20],
    #     'max_depth' : [1,5,10,50,100],
    #     'criterion' :['gini', 'entropy'],
    #     'class_weight': [{0:15,1:1},{0:10,1:1},'balanced',{0:1,1:10}],
    #     'n_jobs':[-1],
    # }

    dtc = DecisionTreeClassifier()  # max_features=5

    CV_dtc = GridSearchCV(estimator=dtc, param_grid=param_grid, cv= 5, n_jobs=-1)
    CV_dtc.fit(x, y)

    CV_dtc.best_params_

    return CV_dtc.best_params_

rfc_param_grid = { 
        'n_estimators': [2,5,10,20,50,100, 200,300,400,500,600],
        'max_features': ['auto', 'sqrt', 'log2',1,2,3,4,5,6,7],
        'max_depth' : [1,5,10,40,50,60,100,200],
        'criterion' :['gini'],
        'class_weight': ['balanced'],
        'n_jobs':[-1],
    }

dtc_param_grid = { 
        # 'n_estimators': [2,5,10,20,50,100, 200,300,400,500,600],
        'max_features': ['auto', 'sqrt', 'log2',1,2,3,4,5,6,7],
        'max_depth' : [1,5,10,40,50,60,100,200],
        'criterion' :['gini'],
        'class_weight': ['balanced'],
        # 'n_jobs':[-1],
        # 'num_leafs':[1, 5, 10, 20, 50, 100],
        'random_state':0

    }

# %time rfc_dict = gridSearch_random_forest(x, y,rfc_param_grid)
# print(rfc_dict)

%time dtc_dict = dtree_random_forest(x, y,dtc_param_grid)
print(dtc_dict)

#300 {'class_weight': 'balanced', 'criterion': 'gini', 'max_depth': 50, 'max_features': 5, 'n_estimators': 20, 'n_jobs': -1}
# 1500 {'class_weight': 'balanced', 'criterion': 'gini', 'max_depth': 100, 'max_features': 10, 'n_estimators': 50, 'n_jobs': -1}
# 1500 {'class_weight': 'balanced', 'criterion': 'gini', 'max_depth': 50, 'max_features': 'sqrt', 'n_estimators': 50, 'n_jobs': -1}

# colsfeat
# 10K {'class_weight': 'balanced', 'criterion': 'gini', 'max_depth': 1, 'max_features': 'sqrt', 'n_estimators': 2, 'n_jobs': -1}

# DecisionTreeClassifier(
#     class_weight='balanced', 
#     criterion='gini', 
#     max_depth=1,
                       
#     max_features='auto', max_leaf_nodes=None,
#                        min_impurity_decrease=0.0, min_impurity_split=None,
#                        min_samples_leaf=1, min_samples_split=2,
#                        min_weight_fraction_leaf=0.0, presort=False,
#                        random_state=None, splitter='best')

# {'class_weight': 'balanced', 'criterion': 'gini', 'max_depth': 40, 'max_features': 5}
