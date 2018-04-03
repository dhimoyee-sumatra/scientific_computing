
from newtdd import newtdd
from nest   import nest
from numpy  import linspace
from pylab  import plot, show
from splinecoeff import splinecoeff
from splineplot import splineplot

#Question 1
xdata1 = [1960,1970]
ydata1 = [3039585530, 3707475887]
plot(xdata1,ydata1,'ro')
interpolant = newtdd(xdata1,ydata1)
x = linspace(1950,2000, 10, endpoint=True)
y = nest(interpolant,x,xdata1)
plot(x,y,'b')
show()

xdata2 = [1960,1970,1990]
ydata2 = [3039585530, 3707475887, 5281653820]
plot(xdata2,ydata2,'ro')
interpolant = newtdd(xdata2,ydata2)
x = linspace(1950,2000, 10, endpoint=True)
y = nest(interpolant,x,xdata2)
plot(x,y,'b')
show()

xdata3 = [1960,1970,1990,2000]
ydata3 = [3039585530, 3707475887, 5281653820, 6079603571]
plot(xdata3,ydata3,'ro')
interpolant = newtdd(xdata3,ydata3)
x = linspace(1950,2000, 10, endpoint=True)
y = nest(interpolant,x,xdata3)
plot(x,y,'b')
show()

#Question 2

x1= [1800, 1850, 1900, 2000]
y1= [280, 283, 291, 370]
splineplot(x1,y1,100)
splinecoeff(x1,y1)
show()



# Question 3
x2= [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003]
y2= [67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777]
plot(x2,y2,'ro')
interpolant = newtdd(x2,y2)
x = linspace(1995,2004, 10, endpoint=True)
y = nest(interpolant,x,x2)
plot(x,y,'b')
splineplot(x2,y2,100)
splineplot(x2,y2,100,4)
splineplot(x2,y2,100,5)
show()