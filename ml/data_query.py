import numpy as np
import pandas as pd
from sklearn import datasets  # sample dataset
import ml.data_load as data_load
# from ml.data_load import df
import ml.modeling as modeling
from importlib import reload
import matplotlib.pyplot as plt  # Matlab-style plotting
# %matplotlib inline

reload(modeling)  # to reload module if we made some changes

cols1 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

cols2 = ['DOB_YY', 'AB_AVEN1', 'AB_AVEN6', 'AB_SURF', 'AB_ANTI', 'AB_SEIZ', 'F_AB_VENT', 'F_AB_VENT6',
         'F_AB_NIUC', 'F_AB_SURFAC', 'F_AB_ANTIBIO', 'F_AB_SEIZ', 'NO_ABNORM', 'AB_NICU']

df = data_load.fetchCollumns(cols1, extra_query='') #extra_query='LIMIT 100'
# df.isnull().sum()
df = df[df.AB_NICU != "U"] #Drop Column with U Unknown 
df = df[df.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan

%time modeling.label_encoding(df) #If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
# y = df.AB_NICU.values

# df.AB_NICU.unique()
# df.AB_NICU.isna().sum()
# print (df[df.AB_NICU == "U"].shape[0])
# df = df[df.AB_NICU != "U"]
# df = df[df.AB_NICU != " "]
# df.shape

%time model, x_train, x_test, y_train, y_test = modeling.random_forest(x, y)  # create model and fit
model.score(x_test, y_test)  # check model score
modeling.get_confusion_matrix(model, x_test, y_test)  # print confusion matrix
model.get_params,model.feature_importances_

important_features = pd.Series(data=model.feature_importances_,index=x.columns)
important_features.sort_values(ascending=False,inplace=True)
important_features

#plot graph of most import feature
important_features.plot(kind = 'bar')
plt.show() # if run outside iPython