import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt  # Matlab-style plotting
# %matplotlib inline

def label_encoding(df):
    # Categorical boolean mask
    categorical_feature_mask = df.dtypes == object
    # filter categorical columns using mask and turn it into a list
    categorical_cols = df.columns[categorical_feature_mask].tolist()

    le = LabelEncoder()
    # apply le on categorical feature columns
    df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))
    return df


# Random Forests
def random_forest(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = RandomForestClassifier(n_estimators=100, oob_score=True, n_jobs=-1, **params)  # max_features=5
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test


# Support Vector Machine
def support_vector_machine(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = SVC(**params)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test


# Confusion Matrix
def get_confusion_matrix(model, x_test, y_test):
    y_pred = model.predict(x_test)
    return confusion_matrix(y_test, y_pred)


# xgb_classifier
def xgb_classifier(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = XGBClassifier(nthread = -1, n_jobs = -1, **params)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

# Feature Importance Applies to XGB and Random Forest Only
def get_feature_importance(x,prediction_model):
    prediction_model.get_params,prediction_model.feature_importances_

    important_features = pd.Series(data=prediction_model.feature_importances_,index=x.columns)
    important_features.sort_values(ascending=False,inplace=True)
    important_features

    #plot graph of most import feature
    important_features.plot(kind = 'bar')
    return plt.show() # if run outside iPython