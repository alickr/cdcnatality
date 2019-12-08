# import random search, random forest, iris data, and distributions
from sklearn.model_selection import RandomizedSearchCV
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import uniform, truncnorm, randint
from pprint import pprint

# get iris data
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
import ml.data_load as data_load
from ml.selected_columns import selected_columns
import ml.modeling as modeling

df = data_load.fetch_rand_data(selected_columns,rows_per_year=100000) #pull random 2000 rec per year
# df = data_load.fetchCollumns(selected_columns, extra_query='LIMIT 1000') #extra_query='LIMIT 100'
# df.isnull().sum()
df = df[df.AB_NICU != "U"] #Drop Column with U Unknown 
df = df[df.AB_NICU != " "] #Drop Empty Space Columsn Not Treated as Nan
modeling.label_encoding(df) #If Data is not encoded
x = df.loc[:, ~df.columns.isin(['AB_NICU', 'DOB_YY'])]  # Remove Specific column by name
y = df.AB_NICU.values
from sklearn.model_selection import GridSearchCV

def random_searchCV_rfc(x,y):
    model_params = {
        # randomly sample numbers from 4 to 204 estimators
        # 'n_estimators': randint(1,200),
        'n_estimators': [1, 20, 30, 300, 500, 800, 1000],
        # normally distributed max_features, with mean .25 stddev 0.1, bounded between 0 and 1
        # 'max_features': truncnorm(a=0, b=1, loc=0.25, scale=0.1),
        'max_features': [0.1,0.3,0.6,10,20,100],

        # uniform distribution from 0.01 to 0.2 (0.01 + 0.199)
        # 'min_samples_split': uniform(0.01, 0.199),
        'n_jobs': [-1],
        'criterion':['gini', 'entropy'],
        'class_weight':['balanced',{0:1,1:2},{0:1,1:3}],
        }

    # create random forest classifier model
    rf_model = RandomForestClassifier()

    # set up random search meta-estimator
    # this will train 100 models over 5 folds of cross validation (500 models total)
    # clf = GridSearchCV(rf_model, model_params, n_iter=30, cv=5, random_state=0,n_jobs=-1)
    clf = GridSearchCV(rf_model, model_params, cv=5,n_jobs=-1)

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

    best_parameters = model.best_estimator_.get_params()
    return best_parameters


# --- CODE BELOW FOR TESTING ONLY --- #
random_searchCV_rfc(x,y)
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