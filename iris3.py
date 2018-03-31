# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:37:48 2018

@author: UttamSinha
"""
from sklearn.datasets import load_iris
from sklearn import datasets
iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred =  gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum()))


data = load_iris()
data.target[[10,25,50]]
#array([0,0,1])
list(data.target_names)
print(data.target_names)