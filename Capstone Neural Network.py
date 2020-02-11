import sklearn #1
import pandas #3
import matplotlib.pyplot as plt #4
import seaborn as sns # visualization #4
import numpy as np #5
from sklearn.utils import shuffle #8
from sklearn.neural_network import MLPClassifier #10
from sklearn.model_selection import cross_validate #14

data=pandas.read_csv("output.txt",header=None)#(place "header=None" into parenthesis to show header #3
print(data) #3

sns.pairplot( data=data,vars=(2,3,4,5,6,7,8,9,10,11,12,13), hue=14)
plt.show() #4

data=np.array(data) #5

X=data[:,2:13] #This gets all the rows and only the first 4 columns. #6
y=data[:,13] #Gets only the 4th row #6
print(X.shape) #(150,4) #6
print(y.shape) #(150,1) #6

X,y=shuffle(X,y,random_state=0) #8

trainX=X[:2724] #9
trainy=y[:2724] #9
testX=X[2724:3627] #9
testy=y[2724:3627] #9

# ~ for layerSize in range(1,12):
clf = MLPClassifier(hidden_layer_sizes=[5,5], random_state=53690)

clf.fit(trainX, trainy)

print(clf.score(trainX,trainy)) #13
print(clf.score(testX,testy)) #13

cv_results=cross_validate(clf, X, y, cv=4) #14
print(cv_results) #14

parameters={'hidden_layer_sizes':([1], [2], [3], [4], [5], [6], [7])}
from sklearn.model_selection import GridSearchCV
cv_results = GridSearchCV(clf,parameters)
print(cv_results)
