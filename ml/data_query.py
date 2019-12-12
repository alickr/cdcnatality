import numpy as np
import pandas as pd
from sklearn import datasets  # sample dataset
import ml.data_load as data_load
import ml.modeling as modeling
from importlib import reload
import matplotlib.pyplot as plt  # Matlab-style plotting
from ml.selected_columns import selected_columns,cols_feat # Columns to Select From SQL Database
from ml.feat_eng import impute # Feature Engineering
# %matplotlib inline
reload(modeling)  # to reload module if we made some changes

selected_columns
%time df_full = data_load.fetch_rand_data(selected_columns,rows_per_year=25000) #pull random 2000 rec per year
# df = data_load.fetchCollumns(selected_columns, extra_query='LIMIT 1000') #extra_query='LIMIT 100'
# df_full.head()
df = df_full[df_full.DOB_YY != 2018]
df_test = df_full[df_full.DOB_YY == 2018]

# --- 2018 is used exclusively for Test Dataset and The rest (2014,2015,2016 & 2017) are used as the Training Dataset --- #
# %time df = data_load.fetchCollumns(selected_columns, extra_query='WHERE DOB_YY <> 2018 ') #extra_query='LIMIT 100'
# %time df_test = data_load.fetchCollumns(selected_columns, extra_query='WHERE DOB_YY = 2018') #extra_query='LIMIT 100'

# Perform Feature Engineering and Imputaions
df = impute(df)
modeling.label_encoding(df) #If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values

rfc_params = {
    # # 'bootstrap': False,
    # 'class_weight': 'balanced',
    # # 'class_weight': {0:1,1:10},
    # 'criterion': 'gini',
    # # 'max_depth': None,
    # # 'max_features': 0.3400028843787042,
    # # 'max_features': 5,
    # # 'max_leaf_nodes': None,
    # # 'min_impurity_decrease': 0.0,
    # # 'min_impurity_split': None,
    # # 'min_samples_leaf': 1,
    # # 'min_samples_split': 0.024136175581379503,
    # # 'min_weight_fraction_leaf': 0.0,
    # 'n_estimators': 50,
    # 'n_jobs': -1,
    # # 'oob_score': False,
    # 'random_state': 0,
    # # 'verbose': 0,
    # # 'warm_start': False
    }

dtc_params = {'class_weight': 'balanced', 'criterion': 'gini', 'max_depth': 40, 'max_features': 5}


# ''' Decision Tree Classifier '''
print("\n---------------------------\nDecision Tree Classifier\n---------------------------")
%time decision_tree_classifier_model, x_train5, x_test5, y_train5, y_test5 = modeling.decision_tree_classifier(x, y,**dtc_params)  # create model and fit
print(decision_tree_classifier_model.score(x_test5, y_test5))  # check model score
print(modeling.get_confusion_matrix(decision_tree_classifier_model, x_test5, y_test5)) # print confusion matrix
print(modeling.get_normalized_confusion_matrix(decision_tree_classifier_model, x_test5, y_test5))  # print Normalized confusion matrix
print(modeling.get_feature_importance(x,decision_tree_classifier_model)) # Plot Feature Importance

# # Logistic Regression Classifier
print("\n---------------------------\nlogistic regression classifier\n---------------------------")
%time logistic_regression_classifier_model, x_train6, x_test6, y_train6, y_test6 = modeling.logistic_regression_classifier(x, y)  # create model and fit
print(logistic_regression_classifier_model.score(x_test6, y_test6))  # check model score
print(modeling.get_confusion_matrix(logistic_regression_classifier_model, x_test6, y_test6)) # print confusion matrix
print(modeling.get_normalized_confusion_matrix(logistic_regression_classifier_model, x_test6, y_test6))  # print Normalized confusion matrix
# print(modeling.get_feature_importance(x,logistic_regression_classifier_model)) # Plot Feature Importance

# Random Forests
print("\n---------------------------\nRANDOM FOREST\n---------------------------")
%time random_forest_model, x_train1, x_test1, y_train1, y_test1 = modeling.random_forest(x, y,**rfc_params)  # create model and fit # class_weight="balanced" class_weight={0:1,1:10}
print(random_forest_model.score(x_test1, y_test1))  # check model score
print(modeling.get_confusion_matrix(random_forest_model, x_test1, y_test1))  # print confusion matrix
print(modeling.get_normalized_confusion_matrix(random_forest_model, x_test1, y_test1))  # print Normalized confusion matrix
print(modeling.get_feature_importance(x,random_forest_model)) # Plot Feature Importance

# XGBoost
print("\n---------------------------\nXGB\n---------------------------")
%time xgb_model, x_train3, x_test3, y_train3, y_test3 = modeling.xgb_classifier(x, y)  # create model and fit
print(xgb_model.score(x_test3, y_test3))  # check model score
print(modeling.get_confusion_matrix(xgb_model, x_test3, y_test3)) # print confusion matrix
print(modeling.get_normalized_confusion_matrix(xgb_model, x_test3, y_test3))  # print Normalized confusion matrix
print(modeling.get_feature_importance(x,xgb_model)) # Plot Feature Importance

# Support Vector Machine Classifier (SVC)
print("\n---------------------------\nSVM\n---------------------------")
%time svm_model, x_train3, x_test3, y_train3, y_test3 = modeling.support_vector_machine(x, y)  # create model and fit
print(svm_model.score(x_test3, y_test3))  # check model score
print(modeling.get_confusion_matrix(svm_model, x_test3, y_test3)) # print confusion matrix
print(modeling.get_normalized_confusion_matrix(svm_model, x_test3, y_test3))  # print Normalized confusion matrix

''' --- PERFORMING ON THE TEST DATASET --- '''
# df_test = df_test[df_test.AB_NICU != "U"] #Drop Column with U Unknown
# df_test = df_test[df_test.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan
%time df_test = data_load.fetchCollumns(selected_columns, extra_query='WHERE DOB_YY = 2018 ') #extra_query='LIMIT 100'

df_test = impute(df_test)

modeling.label_encoding(df_test) #If Data is not encoded

df_test_X = df_test.loc[:, ~df_test.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
df_test_Y = df_test.AB_NICU.values

df_test.AB_NICU.unique()
df_test.shape
print (df_test[df_test.AB_NICU == 0].shape[0])
print (df_test[df_test.AB_NICU == 1].shape[0])


print("\n---------------------------\nDecision TREE TEST DATA\n---------------------------")
print(modeling.get_normalized_confusion_matrix(decision_tree_classifier_model, df_test_X, df_test_Y))  # print Normalized confusion matrix
print(modeling.get_confusion_matrix(decision_tree_classifier_model, df_test_X, df_test_Y))  # print confusion matrix
dt_df_pred = decision_tree_classifier_model.predict(df_test_X).score
decision_tree_classifier_model.score
print("\n---------------------------\nLogistic Regression Classifier TEST DATA\n---------------------------")
print(modeling.get_normalized_confusion_matrix(logistic_regression_classifier_model, df_test_X, df_test_Y))  # print Normalized confusion matrix
print(modeling.get_confusion_matrix(logistic_regression_classifier_model, df_test_X, df_test_Y))  # print confusion matrix
logistic_df_pred = logistic_regression_classifier_model.predict(df_test_X)

print("\n---------------------------\nRANDOM FOREST TEST DATA\n---------------------------")
print(modeling.get_normalized_confusion_matrix(random_forest_model, df_test_X, df_test_Y))  # print Normalized confusion matrix
print(modeling.get_confusion_matrix(random_forest_model, df_test_X, df_test_Y))  # print confusion matrix
rfc_df_pred = random_forest_model.predict(df_test_X)

print("\n---------------------------\nXGB  TEST DATA\n---------------------------")
print(modeling.get_normalized_confusion_matrix(xgb_model, df_test_X, df_test_Y))  # print Normalized confusion matrix
print(modeling.get_confusion_matrix(xgb_model, df_test_X, df_test_Y))  # print confusion matrix
xgb_df_pred = xgb_model.predict(df_test_X)

print("\n---------------------------\nSVM  TEST DATA\n---------------------------")
print(modeling.get_normalized_confusion_matrix(svm_model, df_test_X, df_test_Y))  # print Normalized confusion matrix
print(modeling.get_confusion_matrix(svm_model, df_test_X, df_test_Y))  # print confusion matrix
svm_df_pred = svm_model.predict(df_test_X)

'''
Decision TREE TEST DATA
---------------------------
          Predicted NO  Predicted YES
True NO       0.912197       0.892315
True YES      0.087803       0.107685
          Predicted NO  Predicted YES
True NO        3057622         304896
True YES        294310          36795

'''