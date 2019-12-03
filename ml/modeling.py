import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import xgboost as xgb
from xgboost.sklearn import XGBClassifier


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
def random_forest(x, y, test_size=0.33, random_state=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size, random_state)
    model = RandomForestClassifier(n_estimators=100, oob_score=True, **params)  # max_features=5
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test


# Support Vector Machine
def support_vector_machine(x, y, test_size=0.33, random_state=0):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size, random_state, **params)
    model = SVC()
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test


# Confusion Matrix
def confusion_matrix(model, x_test, y_test):
    y_pred = model.predict(x_test)
    return confusion_matrix(y_test, y_pred)


# xgb_classifier
def xgb_classifier(x, y, test_size=0.33, random_state=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size, random_state)
    model = XGBClassifier(**params)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test
