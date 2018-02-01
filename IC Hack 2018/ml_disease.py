# Mortality Rate model

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset= pd.read_csv('ml_disease.csv')

x = dataset.iloc[:,:5].values
y = dataset.iloc[:,-2].values

print y
pd.DataFrame(dataset)

#Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
"""x[:,1] = labelencoder_x.fit_transform(x[:, 1])
onehotencoder = OneHotEncoder(categorical_features = [1])
x[:,3] = labelencoder_x.fit_transform(x[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
x = onehotencoder.fit_transform(x).toarray()"""

x[:,0] = labelencoder_x.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x[:,2] = labelencoder_x.fit_transform(x[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [2])
x[:,4] = labelencoder_x.fit_transform(x[:, 4])
onehotencoder = OneHotEncoder(categorical_features = [4])
x = onehotencoder.fit_transform(x).toarray()

#Avoiding Dummy Variable Trap
x = x[:,1:]
pd.DataFrame(x)

#Splitting the dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300,random_state = 0)
regressor.fit(x_train,y_train)
# Predicting the Test Result
y_pred = regressor.predict(x_test)


pd.DataFrame(y_test,y_pred)

import statsmodels.formula.api as sm
x = np.append(arr = np.ones((40,1)).astype(int), values = x, axis = 1) #building b0x0 where x0 = 1

print x
x_opt = x[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = x_opt).fit() #fitting the full model with all possible predictors
regressor_OLS.summary()

# Probability of Spread
#Importing the dataset
dataset= pd.read_csv('ml_disease.csv')

x2 = dataset.iloc[:,:5].values
y2 = dataset.iloc[:,-1].values

print y2
pd.DataFrame(dataset)

#Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x2 = LabelEncoder()

x2[:,0] = labelencoder_x2.fit_transform(x2[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x2[:,2] = labelencoder_x2.fit_transform(x2[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [2])
x2[:,4] = labelencoder_x2.fit_transform(x2[:, 4])
onehotencoder = OneHotEncoder(categorical_features = [4])
x2 = onehotencoder.fit_transform(x2).toarray()

#Avoiding Dummy Variable Trap
x2 = x2[:,1:]
pd.DataFrame(x2)

#Splitting the dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size = 0.2, random_state = 0)

#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)"""

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor()
regressor.fit(x2_train,y2_train)
# Predicting the Test Result
y2_pred = regressor.predict(x2_test)


pd.DataFrame(y2_test,y2_pred)

import statsmodels.formula.api as sm
x2 = np.append(arr = np.ones((40,1)).astype(int), values = x2, axis = 1) #building b0x0 where x0 = 1

print x2
x2_opt = x2[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y2, exog = x2_opt).fit() #fitting the full model with all possible predictors
regressor_OLS.summary()
