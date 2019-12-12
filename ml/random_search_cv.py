# import random search, random forest, iris data, and distributions
from sklearn.model_selection import RandomizedSearchCV
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import uniform, truncnorm, randint
from pprint import pprint
from ml.feat_eng import impute # Feature Engineering

# get iris data
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
import ml.data_load as data_load
from ml.selected_columns import selected_columns
import ml.modeling as modeling

%time df = data_load.fetch_rand_data(selected_columns,rows_per_year=10000) #pull random 2000 rec per year
# %time df = data_load.fetchCollumns(selected_columns, extra_query=' ') #extra_query='LIMIT 100'
# df.isnull().sum()
df = impute(df)
modeling.label_encoding(df) #If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values

def random_searchCV_rfc(x,y):
    # model_params1 = {
    #     # randomly sample numbers from 4 to 204 estimators
    #     # 'n_estimators': randint(1,200),
    #     'n_estimators': [1, 20, 30, 300, 500, 800, 1000],
    #     # normally distributed max_features, with mean .25 stddev 0.1, bounded between 0 and 1
    #     # 'max_features': truncnorm(a=0, b=1, loc=0.25, scale=0.1),
    #     'max_features': [0.1,0.6,10,20,100],

    #     # uniform distribution from 0.01 to 0.2 (0.01 + 0.199)
    #     # 'min_samples_split': uniform(0.01, 0.199),
    #     'n_jobs': [-1],
    #     'criterion':['gini', 'entropy'],
    #     'class_weight':['balanced',{0:1,1:0},{0:10,1:1}],
    #     }

    model_params = { 
        'n_estimators': [1,2,5,10,20,50,100, 500],
        'max_features': ['auto', 'sqrt', 'log2'],
        'max_depth' : [1,5,10,50,100],
        'criterion' :['gini', 'entropy'],
        'class_weight': [{0:15,1:1},{0:10,1:1},'balanced',{0:1,1:10}],
        'n_jobs':[-1]
        }

    # create random forest classifier model
    rf_model = RandomForestClassifier()

    # set up random search meta-estimator
    # this will train 100 models over 5 folds of cross validation (500 models total)
    # clf = GridSearchCV(rf_model, model_params, n_iter=30, cv=5, random_state=0,n_jobs=-1)
    clf = RandomizedSearchCV(rf_model, model_params, cv=5,n_jobs=-1,n_iter=100)

    # train the random search meta-estimator to find the best model out of 100 candidates
    model = clf.fit(x, y)

    # print winning set of hyperparameters
    # pprint(model.best_estimator_.get_params()) # Should Uncomment To Test

    # generate predictions using the best-performing model
    # predictions = model.predict(x) # Should Uncomment To Test
    # print(predictions) # Should Uncomment To Test

    best_parameters = model.best_estimator_.get_params()
    return best_parameters

def random_searchCV_xgb(x,y):
    clf_xgb = xgb.XGBClassifier(objective = 'binary:logistic')
    param_dist = {'n_estimators': stats.randint(150, 1000),
                'learning_rate': stats.uniform(0.01, 0.6),
                'subsample': stats.uniform(0.3, 0.9),
                'max_depth': [3, 4, 5, 6, 7, 8, 9],
                'colsample_bytree': stats.uniform(0.5, 0.9),
                'min_child_weight': [1, 2, 3, 4]
                }

    numFolds = 5
    kfold_5 = cross_validation.KFold(n = len(X), shuffle = True, n_folds = numFolds)

    clf = RandomizedSearchCV(clf_xgb, 
                            param_distributions = param_dist,
                            cv = kfold_5,  
                            n_iter = 5, # you want 5 here not 25 if I understand you correctly 
                            scoring = 'roc_auc', 
                            error_score = 0, 
                            verbose = 3, 
                            n_jobs = -1)
    best_parameters = model.best_estimator_.get_params()
    return best_parameters


# --- CODE BELOW FOR TESTING ONLY --- #
%time rfc_dict = random_searchCV_rfc(x,y)
print(rfc_dict)

'''
Random Forest 
{'bootstrap': True,
 'class_weight': 'balanced',
 'criterion': 'entropy',
 'max_depth': None,
 'max_features': 0.3400028843787042,
 'max_leaf_nodes': None,
 'min_impurity_decrease': 0.0,
 'min_impurity_split': None,
 'min_samples_leaf': 1,
 'min_samples_split': 0.024136175581379503,
 'min_weight_fraction_leaf': 0.0,
 'n_estimators': 10,
 'n_jobs': -1,
 'oob_score': False,
 'random_state': None,
 'verbose': 0,
 'warm_start': False}
 '''