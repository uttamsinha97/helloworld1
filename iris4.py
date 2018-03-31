# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:00:42 2018

@author: UttamSinha
"""
from sklearn.datasets import load_iris
data = load_iris()
data.target[[10,25,50]]
#array([0,0,1])
list(data.target_names)
print(data.target_names)