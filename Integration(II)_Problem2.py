import math
def f(x) : 
    return math.sin(x)**2/(x*x)
    
def simp(b):
    s,a = 0,0.000001
    h = b/100000
    for k in range(0,100000,2) :
         s = s + f(a) + 4*f(a+h) + f(a+2*h)
         a = a + 2*h
    return 2*s*h/3

print(simp(10000))