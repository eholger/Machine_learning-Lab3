import numpy as np
import math

#Dimensions of matrices 
rows = 7 
cols = 4
depth = 5

#Creating matrices
A = np.zeros((rows,cols)) #2D Matix of zeros
unique = (0,1,2,3)
A = np.array([unique])
print(A.shape)
A = np.zeros((depth,rows,cols)) #3D Matrix of zeros
A = np.ones((rows,cols)) # 2D Matrix of ones
A = np.array([(1,2,3),(4,5,6),(7,8,9)]) # 2D 3x3 matrix with values
#Turn it into a square diagonal matrix with zeros of-diagonal
d = np.diag(A) #Get diagonal as a row vector
print (d)
d = np.diag(d) #Turn a row vector into a diagonal matrix
print (A)
print (d)

# this works
print(1.0/A)

#Reshapes an array of N to an array of N,1
a = np.array((1,2,3))
print (a.shape)
print (a.reshape(-1,1).shape)
print (a.reshape(1,-1).shape)
print (a.reshape(1,-1).reshape(-1).shape)

# Substract a vector using for loop 
X = np.array([(1,2,3),(4,5,6),(7,8,9)])
u = np.array((1,2,3))

for i_row in range(0,X.shape[0]):
	X[i_row,:] = X[i_row,:]-u

print ('substarcted array')
print (X)

# Subtract using broadcasting
X = np.array([(1,2,3), (4,5,6),(7,8,9)])
u = np.array((1,2,3))
X = X - u

print ('using broadcasting')
print (X)

print (np.sum(u))
