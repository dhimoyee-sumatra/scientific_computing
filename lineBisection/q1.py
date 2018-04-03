import numpy as np
import matplotlib.pyplot as plt
from bisection import *

def f_eg_1_1(x):
    return 2* (np.power(x, 3)) -6 * x - 1

x = np.arange(-2, 2, 0.01)

tol = .5e-6

print "the appro root for 2x^3 -6x -1 = 0 is", bisect(f_eg_1_1, -2, -1, tol)
print "the appro root for 2x^3 -6x -1 = 0 is", bisect(f_eg_1_1, -0.5, 0.5, tol)
print "the appro root for 2x^3 -6x -1 = 0 is", bisect(f_eg_1_1, 1, 2, tol)

plt.plot(x, f_eg_1_1(x), label='1.1.3(a)')
plt.ylim([-5, 5])
plt.xlim([-2,2])
plt.grid(True)
plt.legend(loc =0, borderaxespad= 0)

plt.show()





