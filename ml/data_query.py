import numpy as np
import pandas as pd
from sklearn import datasets  # sample dataset
import ml.data_load as data_load
# from ml.data_load import df
import ml.modeling as modeling
from importlib import reload

reload(modeling)  # to reload module if we made some changes

cols1 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

cols2 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

df = data_load.fetchCollumns(cols1, extra_query=' limit 100000000')
modeling.label_encoding(df)  # If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values

random_forest_model, x_train1, x_test1, y_train1, y_test1 = modeling.random_forest(x, y)  # create model and fit

random_forest_model.score(x_test1, y_test1)  # check model score
modeling.get_confusion_matrix(random_forest_model, x_test1, y_test1)  # print confusion matrix

svm_model, x_train2, x_test2, y_train2, y_test2 = modeling.support_vector_machine(x, y)  # create model and fit

svm_model.score(x_test2, y_test2)  # check model score
modeling.get_confusion_matrix(svm_model, x_test2, y_test2)  # print confusion matrix

xgb_model, x_train3, x_test3, y_train3, y_test3 = modeling.xgb_classifier(x, y)  # create model and fit

xgb_model.score(x_test3, y_test3)  # check model score
modeling.get_confusion_matrix(xgb_model, x_test3, y_test3)  # print confusion matrix
