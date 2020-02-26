import sklearn 
import pandas 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np 
from sklearn.utils import shuffle 
from sklearn.neural_network import MLPClassifier 
from sklearn.model_selection import cross_validate 

data=pandas.read_csv("output.txt",header=None)
print(data) 

sns.pairplot( data=data,vars=(2,3,4,5,6,7,8,9,10,11,12,13), hue=14)
plt.show() 

data=np.array(data) 

X=data[:,2:14]
y=data[:,-1] 
print(X.shape) 
print(y.shape) 

X,y=shuffle(X,y,random_state=0) 

trainX=X[:2724,:] 
trainy=y[:2724] 
testX=X[2724:3627,:] 
testy=y[2724:3627] 

clf = MLPClassifier(random_state=5369,max_iter=20000,hidden_layer_sizes=[5, 5])

clf.fit(trainX, trainy)

print(clf.score(trainX,trainy)) 
print(clf.score(testX,testy)) 

cv_results=cross_validate(clf, X, y, cv=14) 
print(cv_results) 

parameters={'hidden_layer_sizes':([1], [2], [3], [4], [5], [6], [7])}
from sklearn.model_selection import GridSearchCV
cv_results = GridSearchCV(clf,parameters)
print(cv_results)
