import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scp

def makeMatrix(n):
	m=(n, n)
	x= np.zeros((m), dtype= np.float)
	for i in range(1, n+1):
		for j in range(1, n+1):
			x[i-1, j-1]= np.abs((i-1)-(j-1))+1.0
	return x

def naiveG(a, b):
	a_copy= np.copy(a)
	b_copy= np.copy(b)
	m= a.shape
	n= m[0]
	for j in range(0, n-1):
		if (abs(a_copy[j, j])< np.finfo(float).eps):
			return
		for i in range(j+1, n):
			mult= a_copy[i, j]/ a_copy[j, j]
			for k in range(j+1, n):
				a_copy[i, k]= a_copy[i, k]- mult* a_copy[j, k]
			b_copy[i]= b_copy[i]- mult* b_copy[j]
	x= np.zeros((n,1), dtype=np.float)
	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			b_copy[i]= b_copy[i]- a_copy[i, j]*x[j]
		x[i]=b_copy[i]/a_copy[i, i]
	return x

def calError(xa,xc, b, A):
	backErrMat= b- A.dot(xa)
	backErr= np.abs(backErrMat).max()
	print "Backward Error: ", backErr

	forwErrMat= xc-xa
	forwErr= np.abs(forwErrMat).max()
	print "Forward Error: ", forwErr

	relBackErr= backErr/np.abs(b).max()
	print "Relative Backward Error: ", relBackErr

	relForwErr= forwErr/np.abs(xc).max()
	print "Relative Forward Error: ", relForwErr

	errorMag= relForwErr/relBackErr
	print "Error Magnification", errorMag

	cond= np.linalg.norm(A, np.inf) * np.linalg.norm(np.linalg.inv(A), np.inf)
	print "Condition Number: ", cond

print "For n=100"
A1= makeMatrix(100)
xc1= np.ones((100, 1))
b1= A1.dot(xc1)
xa1= naiveG(A1, b1)
calError(xa1, xc1, b1, A1)
print"\n"

print "For n=200"
A1= makeMatrix(200)
xc1= np.ones((200, 1))
b1= A1.dot(xc1)
xa1= naiveG(A1, b1)
calError(xa1, xc1, b1, A1)
print"\n"

print "For n=300"
A1= makeMatrix(300)
xc1= np.ones((300, 1))
b1= A1.dot(xc1)
xa1= naiveG(A1, b1)
calError(xa1, xc1, b1, A1)
print"\n"

print "For n=400"
A1= makeMatrix(400)
xc1= np.ones((400, 1))
b1= A1.dot(xc1)
xa1= naiveG(A1, b1)
calError(xa1, xc1, b1, A1)
print"\n"

print "For n=500"
A1= makeMatrix(500)
xc1= np.ones((500, 1))
b1= A1.dot(xc1)
xa1= naiveG(A1, b1)
calError(xa1, xc1, b1, A1)