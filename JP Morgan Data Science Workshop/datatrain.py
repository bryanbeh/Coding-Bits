import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier

kick = pd.read_csv("kick.csv", low_memory=False)
kick.head()

'goal', 'deadline', 'state_changed_at', 'created_at', 'launched_at', 'static_usd_rate'

kick.nunique()

response = kick["state"]
del kick["state"]
response = response.apply(lambda x: 0 if x in ['failed', 'canceled', 'suspended'] else 1)

print(response)
response.unique()

numerical_columns = kick.select_dtypes(include=['float64', 'int64']).columns

X_train, X_test, y_train, y_test = train_test_split(kick[numerical_columns],
                                                    response, random_state=143)
                                                    
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
rf = RandomForestClassifier(n_estimators=50)
rf.fit(X_train, y_train)
y_test_pred3 = rf.predict(X_test)

print("The confusion matrix: \n")
print(confusion_matrix(y_test, y_test_pred3))
print("\nThe classification report:\n")
print(classification_report(y_test, y_test_pred3, digits=3))


                                              
