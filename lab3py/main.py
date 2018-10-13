import labfuns as lfuns
import numpy as np
import math


#generates gaussian distributed data points, X, and corresponding class y?
X, y = lfuns.genBlobs()
print ('labels?')
print (y)
print ('vektor X')
print (X)
print ('test')
print (X[0])
W = [1/float(len(y)) for i in range(0,len(y))]
print ('ww')
print (W)
print (len(W))
print (np.sum(W))
mu, sigma = lfuns.mlParams(X,y,W)

d = np.ones(len(X))
#sum of the vector X men måste dela upp X klassvis mha y, 
#gör det nedan
# mu is a labels x X matrix
print ('mu')
print (mu)

nn = np.ones((2,2))
nnn = np.array((1,2))

print (nn*nnn)

#print (mu)
t = np.zeros((2,len(mu), len(mu)))
tista = [t]
#tista[0] = mu[0]
print (tista)
#lfuns.plotGaussian(X,y,mu,sigma)

prior = lfuns.computePrior(y,W)
print (prior)

N = lfuns.classifyBayes(X,prior,mu,sigma)
print(y)
precent = 0
for i in range(0,len(y)):
	if y[i] == N[i]: 
		precent +=1
precent = precent/float(len(N))
print ('precent')
print (precent)

#Decision Tree Classifier
#classifier = lfuns.DecisionTreeClassifier()

lfuns.testClassifier(lfuns.classifyBayes)
#lfuns.plotBoundary(classifier)

if (0):
	print ('add')
	print (np.absolute(sigma[0]))

	#print (add)
	cl = np.unique(y)

	arr = np.array([0,0,0,0])
	z = np.ones((9,2))
	arr = np.append(arr,z)
	temp = np.array([1,2])
	temp = np.vstack((temp,[3,2]))
	temp = np.vstack((temp,[3,3]))
	#temp.append((3,4))
	arr = np.append(arr,temp)
	print (arr)
	#print (arr[4])
	#print (arr[4][0])
	#print (arr[4][0][0])
	print ('sista')
	#print (arr[5])
	#print (arr[5][0])
	#print (arr[5][0][0])
	print (len(arr))