import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scp

m1= np.array([[2.0,-2.0,-1.0], [4.0,1.0,-2.0], [-2.0,1.0,-1.0]])
b1= np.array([-2.0, 1.0, -3.0])

m2= np.array([[1.0,2.0,-1.0], [0.0,3.0,1.0], [2.0,-1.0,1.0]])
b2= np.array([2.0, 4.0, 2.0])

m3= np.array([[2.0,1.0,-4.0], [1.0,-1.0,1.0], [-1.0,3.0,-2.0]])
b3= np.array([-7.0, -2.0, 6.0])

def naiveG(a, b):
	m= a.shape
	n= m[0]
	for j in range(0, n-1):
		if (abs(a[j, j])< np.finfo(float).eps):
			return
		for i in range(j+1, n):
			mult= a[i, j]/ a[j, j]
			for k in range(j+1, n):
				a[i, k]= a[i, k]- mult* a[j, k]
			b[i]= b[i]- mult* b[j]
	#print b
	x= np.zeros((n), dtype=np.float)
	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			b[i]= b[i]- a[i, j]*x[j]
		x[i]=b[i]/a[i, i]
	return x

print naiveG(m1, b1)
print naiveG(m2, b2)
print naiveG(m3, b3)

m4= scp.hilbert(2)
b4= np.ones(2) #np.array([1,1])
print naiveG(m4, b4)

m5= scp.hilbert(5)
b5= np.ones(5) #array([1,1,1,1,1])
print naiveG(m5, b5)

m6= scp.hilbert(10)
b6= np.ones(10) #array([1,1,1,1,1,1,1,1,1,1])
print naiveG(m6, b6)

def makeMatrix(n):
	m=(n, n)
	x= np.zeros((m), dtype= np.float)
	b= np.zeros((n), dtype= np.float)
	for i in range(1, n+1):
		for j in range(1, n+1):
			x[i-1, j-1]= 1.0/(i+j-1)
		b[i-1]=1
	return x

