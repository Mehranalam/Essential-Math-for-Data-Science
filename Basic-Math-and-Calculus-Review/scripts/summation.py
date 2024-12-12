# summation
from sympy import *

# ∑i= 152i=21 +22 +23 +24 +25 = 30

# summation in python simplfy
sumy = 0
for i in range(1, 6):
    u = 2*i
    sumy += u

# or

summation = sum(2*i for i in range(1, 6))

print(sumy == summation)

i, n = symbols('i n')
summation = sum(2*i ,(i ,1 ,n))

up_to_5 = summation.subs(n ,5)
print(up_to_5.doit())