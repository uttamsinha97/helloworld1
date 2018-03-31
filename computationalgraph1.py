# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:59:13 2017

@author: UttamSinha
"""
from __future__ import print_function
import tensorflow as tf
node1 = tf.constant(3.0 , dtype=tf.float32)
node2 = tf.constant(4.0 , dtype=tf.float32)
print(node1 , node2)
sess = tf.Session()
print(sess.run([node1 , node2]))


node3 = tf.add(node1 , node2)
print('node3 is as stated' ,node3)
print("sess.run(node3):", sess.run(node3))

print(node1)
print(node2)
