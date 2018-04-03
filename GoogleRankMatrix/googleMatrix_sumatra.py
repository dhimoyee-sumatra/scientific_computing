import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scp

def computeG(A, q):
	m= A.shape
	n=m[0]
	csum= np.sum(A, axis=0)
	rsum= np.sum(A, axis=1)
	G= np.zeros(A.shape)
	for i in range(0, n):
		for j in range(0, n):
			nj=rsum[j]
			G[i,j]= (q/n)+ (A[j,i]*(1-q))/nj
	return G


A1= np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

print "Example: "
w1, v1= np.linalg.eig(computeG(A1, 0.15))
print "When q=0.15, p= \n", v1[:,0]/sum(v1[:,0])
print "Page Rank in decreasing order: (15, 13), 14, (11, 10), (9, 12), (5,6,7,8), (2,3), (1,4)"
print "\n"

print "Question 3:"
print "a: \n"
w2, v2= np.linalg.eig(computeG(A1, 0))
print "When q=0, p= \n", v2[:,0]/sum(v2[:,0])
print "The normalized probability of all the page is zero except for page 1 which has the probability of 1."
print "\n"

print "b: \n"
w3, v3= np.linalg.eig(computeG(A1, 0.5))
print "When q=0.5, p= \n", v3[:,0]/sum(v3[:,0])
print "Page Rank in decreasing order: (11, 10), (15, 12), 14, (9, 12), (2, 3), (5, 6, 7, 8), (1, 4). The probability of all pages from 1-8 decreased from the standard example and the probability of rest of the pages increased."
print "\n"

print "The jump probability determines the probability the surfer will choose a random page. Its value determines the distribution of the probability between all the pages.\n"

print "Question 4: \n"
A1[2,7]=2
A1[12,7]=2
w4, v4= np.linalg.eig(computeG(A1, 0.15))
print v4[:,0]/sum(v4[:,0])
print "Page Rank in decreasing order: 15, 11, 13, (14, 12), 10, 4, 7, 9, 3, 6, 5, 2, 1\n"
print "The page rank of 7 is greater than that of 6, so the strategy has succeed. The probability for pages 3, 4, 7, 8, 11, 12 and 14 increased while the rest decreased when compared to the standard example."
print "\n"


print "Question 5: \n"
A2= np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
	[0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]])

w5, v5= np.linalg.eig(computeG(A2, 0.15))
print v5[:,0]/sum(v5[:,0])
print "Page Rank in decreasing order: 15, 11, 14, 12, 7, 8, 9, 1, 5,, 6, 13, 2, 3, 4 "
print "The page rank for 1, 2, 3, 4, 5, 6, 7, 8, 11, 12 and 15 increased and the rest of the pages decreased."
print "\n"

print "Question 6: \n"
A3= np.array([[1, 0, 1, 0, 0, 1],
	[1, 1, 0, 0, 0, 0],
	[0, 1, 1, 0, 0, 0],
	[0, 0, 1, 1, 1, 0],
	[0, 0, 0, 0, 1, 1],
	[0, 0, 0, 0, 1, 1]])

w6, v6= np.linalg.eig(computeG(A3, 0.15))
print "When q=0.15, p= \n", v6[:,0]/sum(v6[:,0])
print "Page Rank in decreasing order: 6, 5, 2, 3, 1, 4"
print "\n"

w7, v7= np.linalg.eig(computeG(A3, 0))
print "When q=0, p= \n", v7[:,0]/sum(v7[:,0])
print "The normalized probability of all the page is zero except for page 1 which has the probability of 1."
print "\n"

w8, v8= np.linalg.eig(computeG(A3, 0.5))
print "When q=0.5, p= \n", v8[:,0]/sum(v8[:,0])
print "The probability of pages 1-4 increased from that of the standard example with p=0.15 while the probability of the rest of pages decreased."
print "Page Rank in decreasing order: 6, 5, (2, 3), 1, 4."
print "\n"







