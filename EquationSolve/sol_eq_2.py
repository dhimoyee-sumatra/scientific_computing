import numpy as np
import matplotlib.pyplot as plt
import math
from bisection import *

#question 4
def f_eq_2(theta):
	x1=5
	x2=0
	y2=6
	l1= 3
	l2= 3* np.sqrt(2)
	l3= 3
	alpha= (np.radians(45))
	p1= 5
	p2= 5
	p3= 3
	a2= (l3* np.cos(theta))-x1
	b2= (l3* np.sin(theta))
	a3= l2* ((np.cos(theta)*np.cos(alpha))- (np.sin(theta)*np.sin(alpha)))- x2
	b3= l2* ((np.cos(theta)* np.sin(alpha))+ (np.sin(theta)*np.cos(alpha)))- y2
	n1= b3*(np.power(p2,2)-np.power(p1,2)-np.power(a2,2)-np.power(b2,2))- b2*(np.power(p3,2)-np.power(p1,2)-np.power(a3,2)-np.power(b3,2))
	n2= -a3*(np.power(p2,2)-np.power(p1,2)-np.power(a2,2)-np.power(b2,2))+ a2*(np.power(p3,2)-np.power(p1,2)-np.power(a3,2)-np.power(b3,2))
	d= 2* (a2*b3 -b2*a3)
	return (np.power(n1,2))+ (np.power(n2,2))- ((np.power(p1,2))* (np.power(d,2)))

tol = .5e-6

print "the appro root is ", bisect(f_eq_2, -1, -0.6, tol)
print "the appro root is ", bisect(f_eq_2, -0.6, 0, tol)
print "the appro root is ", bisect(f_eq_2, 0.5, 1.4, tol)
print "the appro root is ", bisect(f_eq_2, 2, 3, tol)

x= np.linspace(-np.pi, np.pi)
plt.plot(x, f_eq_2(x))
plt.ylim([-50000, 350000])
plt.xlim([-4,4])
plt.grid(True)
plt.show()

theta1= bisect(f_eq_2, -1, -0.6, tol)
theta2= bisect(f_eq_2, -0.6, 0, tol)
theta3= bisect(f_eq_2, 0.5, 1.4, tol)
theta4= bisect(f_eq_2, 2, 3, tol)

def f_eq_3(theta):
	x1=5
	x2=0
	y2=6
	l1= 3
	l2= 3* np.sqrt(2)
	l3= 3
	alpha= (np.radians(45))
	p1= 5
	p2= 5
	p3= 3
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

	plt.ylim([0, 7])
	plt.xlim([-2, 6])
	plt.suptitle('theta=' + str(theta), fontsize=11)
	plt.show()
	return

f_eq_3(theta1)
f_eq_3(theta2)
f_eq_3(theta3)
f_eq_3(theta4)



