import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as scp

def guassSeidel(a, b, xc):
    tol = .5e-6
    n = len(b)
    d = [a[i, i] for i in range(n)]
    r = a - np.diag(d)
    bb = np.reshape(b, (n, 1))
    dd = np.reshape(d, (n, 1))

    xk= np.zeros((n,1))
    xk1= np.zeros((n,1))
    u = np.triu(a, 1)
    l = np.tril(a, -1)
    while (np.abs(xc - xk1).max() > tol):
        for i in range(n):
            xk1[i]=(bb[i]- u[i].dot(xk)-l[i].dot(xk1))/dd[i]
        xk=xk1
    print xk1
    return xk1



A= np.array([[3,-1,0,0,0,.5], [-1,3,-1,0,.5,0], [0,-1,3,-1,0,0], [0,0,-1,3,-1,0],[0,.5,0,-1,3,-1], [.5,0,0,0,-1,3]])
b= np.array([[2.5],[1.5],[1],[1],[1.5],[2.5]])
xc= np.ones((6,1))
guassSeidel(A,b,xc)