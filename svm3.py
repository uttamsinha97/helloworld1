# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:16:58 2018

@author: UttamSinha
"""

from sklearn import svm
X = [[0,0],[1,1]]
y = [0,1]
cld = svm.SVC()
clf.fit(X,y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
