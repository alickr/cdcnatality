from ml.modeling import *
import copy

# --- Importing Dataset ---
# Create a sql engine that connects to AWS RDS
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="dev",
                               pw="rooting",
                               db="cdcnatality"))
                               
# %time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_SURF,AB_ANTI,AB_SEIZ,F_AB_VENT,F_AB_VENT6,F_AB_NIUC,F_AB_SURFAC,F_AB_ANTIBIO,F_AB_SEIZ,NO_ABNORM,AB_NICU FROM all_years_data;', engine)
%time df = pd.read_sql_query('SELECT DOB_YY,AB_AVEN1,AB_AVEN6,AB_SURF,AB_ANTI,AB_SEIZ,F_AB_VENT,F_AB_VENT6,F_AB_NIUC,F_AB_SURFAC,F_AB_ANTIBIO,F_AB_SEIZ,NO_ABNORM,AB_NICU FROM all_years_proper_template;', engine)

df.head()
df.shape

# --- Preparing Data For Training ---
# y = dataset.iloc[:, 4].values
# X = dataset.iloc[:, 0:4].values
df.isnull().any()

%time label_encoding(df)

%time df.corr(method ='pearson')

X = df.loc[:, ~df.columns.isin(['AB_NICU','DOB_YY'])] # Remove Specific column by name
y = df.AB_NICU.values
y

len(y.shape)
# Random Forests
def random_forest2(x, y, test_size_val=0.33, random_state_val=0, **params):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = test_size_val, random_state = random_state_val)
    model = RandomForestClassifier(n_estimators=100, oob_score=True, **params)  # max_features=5
    model.fit(x_train, y_train)
    return model, x_train, x_test, y_train, y_test

rfc = random_forest(X, y)
print(rfc.model)
# ?-------------------------------------------------------------------------------------------------------------------------
# Random Forests
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, y_test = train_test_split(X, y,random_state=0)

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(n_estimators=100,oob_score=True) #max_features=5

random_forest.fit(X_train, Y_train)

Y_pred = random_forest.predict(X_test)

print(random_forest.score(X_train, Y_train))
print(random_forest.get_params,random_forest.feature_importances_)

Y_pred
