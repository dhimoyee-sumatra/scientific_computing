import numpy as np
import matplotlib.pyplot as plt
from bisection import *

def f_eg_1_1(x):
    return (np.exp(x-2)) + np.power(x, 3) - x

x = np.arange(-2, 2, 0.01)

tol = .5e-6

print "the appro root for e^x-2 + x^3 -x = 0 is", bisect(f_eg_1_1, -2, -1, tol)
print "the appro root for e^x-2 + x^3 -x = 0 is", bisect(f_eg_1_1, -0.5, 0.5, tol)
print "the appro root for e^x-2 + x^3 -x = 0 is", bisect(f_eg_1_1, 0.6, 1.6, tol)

plt.plot(x, f_eg_1_1(x), label='1.1.3(b)')
plt.ylim([-3, 3])
plt.xlim([-2,2])
plt.grid(True)
plt.legend(loc =0, borderaxespad= 0)

plt.show()
