# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:45:40 2018

@author: UttamSinha
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:23:30 2018

@author: UttamSinha
"""
import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
#from sklearn.model_selection import train_test_spli
#from sklearn.grid_search import GridSearchCV
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.shape)
print(dataset.head(20))
#print(dataset.head(40))
print(dataset.describe())
print(dataset.groupby('sepal-width').size())
print(dataset.groupby('class').size())
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
dataset.hist()
plt.show()
scatter_matrix(dataset)
plt.show()
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20


#seed = 7
#X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
