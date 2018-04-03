import numpy as np
import matplotlib.pyplot as plt
from bisection import *

# question 1
def f_eq_1(theta):
	x1=4
	x2=0
	y2=4
	l1= 2
	l2= np.sqrt(2)
	l3= np.sqrt(2)
	alpha= (np.radians(90))
	p1= np.sqrt(5)
	p2= np.sqrt(5)
	p3= np.sqrt(5)
	a2= (l3* np.cos(theta))-x1
	b2= (l3* np.sin(theta))
	a3= l2* ((np.cos(theta)*np.cos(alpha))- (np.sin(theta)*np.sin(alpha)))- x2
	b3= l2* ((np.cos(theta)* np.sin(alpha))+ (np.sin(theta)*np.cos(alpha)))- y2
	n1= b3*(np.power(p2,2)-np.power(p1,2)-np.power(a2,2)-np.power(b2,2))- b2*(np.power(p3,2)-np.power(p1,2)-np.power(a3,2)-np.power(b3,2))
	n2= -a3*(np.power(p2,2)-np.power(p1,2)-np.power(a2,2)-np.power(b2,2))+ a2*(np.power(p3,2)-np.power(p1,2)-np.power(a3,2)-np.power(b3,2))
	d= 2* (a2*b3 -b2*a3)
	return (np.power(n1,2))+ (np.power(n2,2))- ((np.power(p1,2))* (np.power(d,2)))

print f_eq_1(np.radians(45))
print f_eq_1(np.radians(-45))

#question 2
tol = .5e-6

print "the appro root is ", bisect(f_eq_1, -2, 0, tol)
print "the appro root is ", bisect(f_eq_1, 0, 2, tol)
x= np.linspace(-np.pi, np.pi)
plt.plot(x, f_eq_1(x))
plt.ylim([-5000, 35000])
plt.xlim([-4,4])
plt.grid(True)
plt.show()

#question 3
#this question repeats the work of question 1 becuase in the first function I did not calculate the value of x and y
def f_eq_2(theta):
	x1=4
	x2=0
	y2=4
	l1= 2
	l2= np.sqrt(2)
	l3= np.sqrt(2)
	alpha= (np.radians(90))
	p1= np.sqrt(5)
	p2= np.sqrt(5)
	p3= np.sqrt(5)
	a2= (l3* np.cos(theta))-x1
	b2= (l3* np.sin(theta))
	a3= l2* ((np.cos(theta)*np.cos(alpha))- (np.sin(theta)*np.sin(alpha)))- x2
	b3= l2* ((np.cos(theta)* np.sin(alpha))+ (np.sin(theta)*np.cos(alpha)))- y2
	n1= b3*(np.power(p2,2)-np.power(p1,2)-np.power(a2,2)-np.power(b2,2))- b2*(np.power(p3,2)-np.power(p1,2)-np.power(a3,2)-np.power(b3,2))
	n2= -a3*(np.power(p2,2)-np.power(p1,2)-np.power(a2,2)-np.power(b2,2))+ a2*(np.power(p3,2)-np.power(p1,2)-np.power(a3,2)-np.power(b3,2))
	d= 2* (a2*b3 -b2*a3)
	x= n1/d
	y= n2/d
	px1=x+ l3* np.cos(theta)
	py1=y+ l3* np.sin(theta)
	px2=x+ l2* np.cos(theta+alpha)
	py2=y+ l2* np.sin(theta+alpha)

	plt.plot([x,px1,px2,x], [y,py1,py2,y])
	plt.plot([0,x],[0,y])
	plt.plot([x1,px1],[0,py1])
	plt.plot([x2,px2],[y2,py2])

	plt.ylim([0, 4])
	plt.xlim([0, 4])
	plt.show()
	return

f_eq_2(np.radians(45))
f_eq_2(np.radians(-45))

