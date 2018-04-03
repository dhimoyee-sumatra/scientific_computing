import numpy as np
import matplotlib.pyplot as plt
from bisection import *

def f_eg_1_1(x):
    return 1 + 5*x -6 * (np.power(x, 3)) - (np.exp(2 * x))

x = np.arange(-2, 2, 0.001)

tol = .5e-6

print "the appro root for 1 + 5x -6x^3 -e^2x = 0 is", bisect(f_eg_1_1, -1.5, -0.5, tol)
print "the appro root for 1 + 5x -6x^3 -e^2x = 0 is", bisect(f_eg_1_1, -0.8, 0.2, tol)
print "the appro root for 1 + 5x -6x^3 -e^2x = 0 is", bisect(f_eg_1_1, 0.3, 1.3, tol)

plt.plot(x, f_eg_1_1(x), label='1.1.3(c)')
plt.ylim([-3, 3])
plt.xlim([-2,2])
plt.grid(True)
plt.legend(loc =0, borderaxespad= 0)


plt.show()
