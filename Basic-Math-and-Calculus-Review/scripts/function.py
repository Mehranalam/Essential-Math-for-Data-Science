# function
from sympy import *

# simple linear function of mathmatics -> 
#y = 2x + 1
def y(x):
    y = 2*x + 1
    return y


for i in range(0,10):
    print(y(i))

x = symbols('x')
y = 2*x + 1
plot(y)

# next chart of y = x ** 2 + 1 
y = x ** 2 + 1
plot(y)


'''
Note that functions utilize multiple input variables, not just one.
 For example, we canhave a function with independent variables x and y.
 Note that y is not dependent likein previous examples.
'''

# f(x, y) = 2x + 2y

from sympy.plotting import plot3d

x, y = symbols('x y')
f = 2*x + 2*y

plot3d(f)