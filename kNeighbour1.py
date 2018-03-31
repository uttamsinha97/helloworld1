# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 02:10:25 2017
@author: UttamSinha
"""

from sklearn.neighbors import NearestNeighbors
import numpy as np
X = np.array([-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
distances , indices = nbrs.kneighbors(X)
indices
array([[0, 1],[1, 0],[2, 1],[3, 4],[4, 3],[5, 4]])
distances
array([[0.,1.],[0.,1.],[0.,1.41421356],[0.,1.],[0.,1.],[0.,1.41421356]])