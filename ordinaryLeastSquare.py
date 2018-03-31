# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:22:51 2018

@author: UttamSinha
"""

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0,0],[1,1],[2,2]],[0,1,2])
#LinearRegression(copy_X=True, fit_intercept=True , n_jobs=1 ,normalise=False)
reg.coef_