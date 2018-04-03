
from numpy import *

def nest(c,x,b=[]):
	d = len(c)-1
	if b==[]:
		b = zeros(d) 
	y = c[d]
	for i in range(d-1,-1,-1):
		y *= (x-b[i])
		y += c[i]
	return y

