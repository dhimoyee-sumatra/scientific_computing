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

def leastSquare(x, y, c):
	n= len(x)
	a= np.ones(n)
	x2= [i**2 for i in x]
	x3= [i**3 for i in x]
	if(c==1):
		A= np.column_stack((a, x))
	if(c==2):
		A= np.column_stack((a, x, x2))
	if(c==3):
		A= np.column_stack((a, x, x2, x3))
	#print A
	AT= np.transpose(A)
	#print AT
	ATA= np.dot(AT, A)
	#print ATA
	ATB= np.dot(AT, y)
	#print ATB
	x = naiveG(ATA, ATB)
	return x

def RMSE(y, x, xc, c):
	n= len(y)
	b= np.ones(n)
	se=0
	if(c==1):
		for i in range(n):
			b[i]= xc[0]+ xc[1]*x[i]
			se+= (b[i]-y[i])*(b[i]-y[i])
	if(c==2):
		for i in range(n):
			b[i]= xc[0]+ xc[1]*x[i]+xc[2]*(x[i]**2)
			se+= (b[i]-y[i])*(b[i]-y[i])
	if(c==3):
		for i in range(n):
			b[i]= xc[0]+ xc[1]*x[i]+xc[2]*(x[i]**2)+ xc[3]*(x[i]**3)
			se+= (b[i]-y[i])*(b[i]-y[i])
	rmse= np.sqrt(se/n)
	print "RMSE: " , rmse
	return b

print "Question 2: "
print "a) "
x1= range(1994, 2004)
y1= [67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777]
val1= leastSquare(x1,y1,1)
b1= RMSE(y1, x1, val1, 1)
print "least square: " , val1
plt.plot(x1, y1, 'g^', x1, b1)
plt.show()
t=2010
v= val1[0]+ val1[1]*t
print "oil production at 2010 is: ", v

print "Question 2: "
print "b) "
val1= leastSquare(x1,y1,2)
b1= RMSE(y1, x1, val1, 2)
print "least square: " , val1
plt.plot(x1, y1, 'g^', x1, b1)
plt.show()
t=2010
v= val1[0]+ val1[1]*t+ val1[2]*(t**2)
print "oil production at 2010 is: ", v

print "Question 2: "
print "c) "
val1= leastSquare(x1,y1,3)
b1= RMSE(y1, x1, val1, 3)
print "least square: " , val1
plt.plot(x1, y1, 'g^', x1, b1)
plt.show()
t=2010
v= val1[0]+ val1[1]*t+ val1[2]*(t**2)+ val1[3]*(t**3)
print "oil production at 2010 is: ", v
print "\n"


print "Question 5: "
print "a) "
x2= [0.59, 0.80, 0.95, 0.45, 0.79, 0.99, 0.90, 0.65, 0.79, 0.69, 0.79, 0.49, 1.09, 0.95, 0.79, 0.65, 0.45, 0.60, 0.89, 0.79, 0.99, 0.85]
y2= [3980, 2200, 1850, 6100, 2100, 1700, 2000, 4200, 2440, 3300, 2300, 6000, 1190, 1960, 2760, 4330, 6960, 4160, 1990, 2860, 1920, 2160]
val2= leastSquare(x2,y2,1)
b2= RMSE(y2, x2, val2, 1)
print "least square: " , val2
plt.plot(x2, y2, 'ro', x2, b2)
plt.show()
print "b) "
print "y= (P-0.23)(9510.10- 8314.36P)"
print "y= -8314.36P^2 + 11422.4P - 2187.32"
print "dy/dP= -16628.72P+ 11422.4"
print "dy/dP= 0"
print "P= 0.6869"
print "\n"

print "Question 10: "
x3= [1.49, 3.03, 0.57, 5.74, 3.51, 3.73, 2.98, -0.18, 6.23, 3.38, 2.15, 2.10, 3.93, 2.47, -0.41]
y3= [44.6, 57.8, 49.9, 61.3, 49.6, 61.8, 49.0, 44.7, 59.2, 53.9, 46.5, 54.7, 50.3, 51.2, 45.7]
val3= leastSquare(x3,y3,1)
b3= RMSE(y3, x3, val3, 1)
print "least square: " , val3
plt.plot(x3, y3, 'g^', x3, b3)
plt.show()
print "percentage points of vote: ", val3[1]




