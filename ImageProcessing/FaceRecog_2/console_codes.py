Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> x = np.array([4,5,3,3,5,6,3,2,4,4,5,4,2,3,4,5,6,6,3,3])
>>> len(x)
20
>>> face_1 = np.array([4,56,1,8,7,4,3,4,5,6,7,8,8,4,23,3,5,7,8])
>>> len(face_1)
19
>>> face_1 = np.array([4,56,1,8,7,4,3,4,5,6,7,8,8,4,23,3,5,7,8,12])
>>> x
array([4, 5, 3, 3, 5, 6, 3, 2, 4, 4, 5, 4, 2, 3, 4, 5, 6, 6, 3, 3])
>>> face_1
array([ 4, 56,  1,  8,  7,  4,  3,  4,  5,  6,  7,  8,  8,  4, 23,  3,  5,
        7,  8, 12])
>>> np.sqrt(sum((x - face_1) ** 2))
56.36488268416781
>>> 1000 / 4
250.0
>>> z = np.zeros((1000,1))
>>> total_faces = 1000
>>> length = 4
>>> for i in range(length):
	print(i*(total_faces/length))

	
0.0
250.0
500.0
750.0
>>> for i in range(length):
	n = total_faces / length
	print(i*(n), i+1 * (n))

	
0.0 250.0
250.0 251.0
500.0 252.0
750.0 253.0
>>> for i in range(length):
	n = total_faces / length
	print(i*n, i+1 * n)

	
0.0 250.0
250.0 251.0
500.0 252.0
750.0 253.0
>>> for i in range(length):
	n = total_faces / length
	print(i*n, (i+1) * n)

	
0.0 250.0
250.0 500.0
500.0 750.0
750.0 1000.0
>>> faces = []
'
>>> faces = ['ravi.npy','unknown.npy']
>>> faces[0]
'ravi.npy'
>>> faces[0].split('.')
['ravi', 'npy']
>>> faces[0].split('.')[0]
'ravi'
>>> 
