import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv('./data/adult.csv')
data.head()

#Data processing - missing values
data['occupation'].replace(to_replace ="?", 
                 value = "Miscellaneous", 
                  inplace = True)

# Label Encoding
le1=LabelEncoder()
occupation=le1.fit_transform(data['occupation'])
occ = dict(zip(occupation, data.occupation))

le2 = LabelEncoder()
gender = le2.fit_transform(data['gender'])
gen = dict(zip(gender, data.gender))

# print(occ)
# print(gen)

#updating the data with new labels
data.occupation = occupation
data.gender = gender

# defining parameters on which model will be trained
X = data[['age','occupation']]
#desired output
Y = data['income']

#split data into training and testing model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 23)

#Training the model 
unbias = OneVsRestClassifier(RandomForestClassifier(),n_jobs=-1)
unbias.fit(X_train,Y_train)

#accuracy
unbias.score(X_train,Y_train)

#test result 
# print(unbias.predict([[50, 11]]))
# print(unbias.predict([[50, 11]]))

#different model accuray
unbias_LR = LogisticRegression()         #accuracy: 0.7478899
unbias_cat = CatBoostClassifier()        #accuracy: 0.7832199
unbias_svm = svm.SVC()                   #accuracy: 0.7602657


#pickle
pickle.dump(unbias, open('unbiased.pkl','wb'))











