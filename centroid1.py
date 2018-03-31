# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 02:24:44 2017
@author: UttamSinha
"""

from sklearn.neighbors.nearest_centroid import NearestCentroid
import numpy as np
X = np.array([[-1, -5], [-2, -5], [-3, -7], [6, 4], [5, 3], [2, 8]])
y = np.array([8, 9, 7, 2, 4, 8])
clf = NearestCentroid()
clf.fit(X,y)
NearestCentroid(metric='euclidean', shrink_threshold=None)
print(clf.predict([[-0.8, -1]]))
