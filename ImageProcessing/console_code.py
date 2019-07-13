Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> labels = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1])
>>> dist = [8,7,9,43,5,7,2,42,12,45,8,4,23,23,4,6,7,8,34]
>>> len(dis)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    len(dis)
NameError: name 'dis' is not defined
>>> len(dist)
19
>>> dist = [18,8,7,9,43,5,7,2,42,12,45,8,4,23,23,4,6,7,8,34]
>>> idx = np.argsort(dist)
>>> idx
array([ 7, 15, 12,  5, 16,  2, 17,  6,  1, 18, 11,  3,  9,  0, 14, 13, 19,
        8,  4, 10], dtype=int64)
>>> labels[idx]
array([0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1])
>>> labels[idx][:5]
array([0, 1, 1, 0, 1])
>>> labels = labels[idx][:5]
>>> np.unique(labels,return_count= True)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    np.unique(labels,return_count= True)
TypeError: unique() got an unexpected keyword argument 'return_count'
>>> np.unique(labels,return_counts= True)
(array([0, 1]), array([2, 3], dtype=int64))
>>> count = np.unique(labels,return_counts= True)
>>> count
(array([0, 1]), array([2, 3], dtype=int64))
>>> count[0]
array([0, 1])
>>> count[1]
array([2, 3], dtype=int64)
>>> np.argmax(count[1])
1
>>> count[0][np.argmax(count[1])]
1
>>> 
