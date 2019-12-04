import numpy as np
import pandas as pd
from sklearn import datasets  # sample dataset
import ml.data_load as data_load
# from ml.data_load import df
import ml.modeling as modeling
from importlib import reload

reload(modeling)  # to reload module if we made some changes

# temp1 = datasets.load_breast_cancer() #dataset as temp1
# x = temp1.data[:, :3]  # we only take the first 3 features.
# y = temp1.target

cols1 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

cols2 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']


df = data_load.fetchCollumns(cols1)
# modeling.label_encoding(df) #If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values

model, x_train, x_test, y_train, y_test = modeling.random_forest(x, y)  # create model and fit

model.score(x_test, y_test)  # check model score
modeling.get_confusion_matrix(model, x_test, y_test)  # print confusion matrix
