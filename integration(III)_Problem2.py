# Link to problems: http://10.33.1.12/~comphy/integration3.html

import math
def f(x,A):
    return 1/math.sqrt(math.fabs(2*A*A-2*x*x))
def fe(x,A):
    return 1/math.sqrt(math.fabs(math.exp(2*A*A)-math.exp(2*x*x)))
F = [f,fe]
    
def simp(b,j):
    s,n,A = 0,10000,b-0.00001
    h = 2*b/n 
    a = -b
    for k in range(0,n,2) :
         s = s + F[j](a,A)+ 4*F[j](a+h,A) + F[j](a+2*h,A)
         a = a + 2*h
    return math.sqrt(2)*s*h/3

for j in range(2):
    for i in range(1,101):
        print(i/10,"   ",simp(i/10,j))
    print(" ")