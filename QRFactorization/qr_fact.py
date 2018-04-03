import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scp

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


def QRleastSquare(A, b):
	n= A.shape[0]
	q, r= np.linalg.qr(A)
	c= np.transpose(q).dot(b)
	r= r[:n, :]
	c= c[:n, :]
	x= naiveG(r, c)
	a= r.dot(x)-c
	print "2-norm error: ", np.linalg.norm(a)
	return x


def computeY(x, d):
	n=len(x)
	y= np.zeros((n,1))
	for a in range (0, n):
		for b in range(0, d+1):
			y[a,0]+= np.power(x[a],b)
	return y



#Question5
A5_1= np.array([[1,1], [2,1], [1, 2], [0, 3]])
b5_1= np.array([[3], [5], [5], [5]])
x5_1= QRleastSquare(A5_1, b5_1)
print x5_1

A5_2= np.array([[1, 2, 2], [2, -1, 2], [3, 1, 1], [1, 1, -1]])
b5_2= np.array([[10], [5], [10], [3]])
x5_2= QRleastSquare(A5_2, b5_2)
print x5_2

#Question6
A6_1= np.array([[3, -1, 2], [4, 1, 0], [-3, 2, 1], [1, 1, 5], [-2, 0, 3]])
b6_1= np.array([[10], [10], [-5], [15], [0]])
x6_1= QRleastSquare(A6_1, b6_1)
print x6_1

A6_2= np.array([[4, 2, 3, 0], [-2, 3, -1, 1], [1, 3, -4, 2], [1, 0, 1, -1], [3, 1, 3, -2]])
b6_2= np.array([[10], [0], [2], [0], [5]])
x6_2= QRleastSquare(A6_2, b6_2)
print x6_2

#Question7
A7= scp.hilbert(10)

A7_1= A7[:,:6]
c=np.ones((6,1))
b7_1=A7_1.dot(c)
x7_1= QRleastSquare(A7_1, b7_1)
print x6_1

A7_2= A7[:,:8]
c=np.ones((8,1))
b7_2=A7_2.dot(c)
x7_2= QRleastSquare(A7_2, b7_2)
print x7_2

#Question8
A8= np.linspace(2, 4, 11)

A8_1= np.vander(A8, 5, True)
b8_1= computeY(A8, 5)
x8_1= QRleastSquare(A8_1, b8_1)
print x8_1

A8_2= np.vander(A8, 6, True)
b8_2= computeY(A8, 6)
x8_2= QRleastSquare(A8_2, b8_2)
print x8_2

A8_3= np.vander(A8, 8, True)
b8_3= computeY(A8, 8)
x8_3= QRleastSquare(A8_3, b8_3)
print x8_3
print "They are equal or slightly off"




