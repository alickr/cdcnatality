import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt  # Matlab-style plotting
# %matplotlib inline
# import seaborn as sns

# Random Forests
def random_forest(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = RandomForestClassifier(**params)  # max_features=5 n_estimators=100, oob_score=True, n_jobs=-1, 
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

# Support Vector Machine
def support_vector_machine(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = SVC(**params)
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

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

def label_encoding(df):
    # Categorical boolean mask
    categorical_feature_mask = df.dtypes == object
    # filter categorical columns using mask and turn it into a list
    categorical_cols = df.columns[categorical_feature_mask].tolist()

    le = LabelEncoder()
    # apply le on categorical feature columns
    df[categorical_cols] = df[categorical_cols].apply(lambda col: le.fit_transform(col))
    return df

# Confusion Matrix
def get_confusion_matrix(model, x_test, y_test):
    y_pred = model.predict(x_test)
    return pd.DataFrame(
            confusion_matrix(y_test, y_pred),
            columns=['Predicted NO', 'Predicted YES'],
            index=['True NO', 'True YES']
        )

    # return confusion_matrix(y_test, y_pred)

def get_normalized_confusion_matrix(classifier, x_test, y_test):
    y_pred = classifier.predict(x_test)
    C = confusion_matrix(y_test, y_pred)
    C = C / C.astype(np.float).sum(axis=0)

    return pd.DataFrame(
            C,
            columns=['Predicted NO', 'Predicted YES'],
            index=['True NO', 'True YES']
        )
    # return C
    
    

    # Return a Seaborn Preaty Graph
    # cm = confusion_matrix(y_test, y_pred,labels=[0, 1])
    # # Normalise
    # cmn = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    # fig, ax = plt.subplots(figsize=(10,10))
    # sns.heatmap(cmn, annot=True, fmt='.2f', xticklabels=['0','1'], yticklabels=['0','1'])
    # plt.ylabel('Actual')
    # plt.xlabel('Predicted')
    # return plt.show(block=False)

    # Support Vector Machine
def decision_tree_classifier(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    # Create Decision Tree classifer object
    model = DecisionTreeClassifier(**params)

    # Train Decision Tree Classifer
    model = model.fit(x_train,y_train)

    #Predict the response for test dataset
    # y_pred = model.predict(X_test)

    return model, x_train, x_test, y_train, y_test

def logistic_regression_classifier(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = LogisticRegression(**params)
    model.fit(x_train, y_train)
    print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(model.score(x_train, y_train)))
    print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(model.score(x_test, y_test)))
    return model, x_train, x_test, y_train, y_test