import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scp

def jacobi(a, b, xc):
	tol = .5e-6
	n= len(b)
	d=[a[i, i] for i in range(n)]
	r= a - np.diag(d)
	x= np.zeros((n,1))
	bb= np.reshape(b, (n,1))
	dd= np.reshape(d, (n,1))
	k=0
	while(np.abs(xc-x).max()> tol):
		x=(bb-np.dot(r,x))/dd
		k=k+1
	print k
	backErrMat = b - a.dot(x)
	backErr = np.abs(backErrMat).max()
	print "Backward Error: ", backErr
	return x

def makeMatrix(n):
	d0=[3 for i in range(n)]
	d1=[-1 for i in range (n-1)]
	d_1=[-1 for i in range (n-1)]
	D= np.diag(d0, 0)+np.diag(d1, 1)+ np.diag(d_1, -1)
	return D

def makeVector(n):
	b= np.zeros((n,1))
	b[0]=2; b[1:n-1]=1; b[n-1]=2
	return b

a1= makeMatrix(100)
b1= makeVector(100)
x1= np.ones((100,1))
print jacobi(a1, b1, x1)

