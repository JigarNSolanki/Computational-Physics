# Link to problems: http://10.33.1.12/~comphy/integration3.html
import math
def f(x):
   return 1/math.sqrt(math.fabs(9.81*(2*math.cos(x)-1)))

def simp(n):
    s,a,b = 0,math.radians(-60)+0.001,0
    h = (b-a)/n
    for k in range(0,n,2) :
         s = s + f(a)+ 4*f(a+h)+f(a+2*h)
         a = a + 2*h
    return 4*s*h/3 

for n in range(1000,5000,100):
    print(n,"  ",simp(n))
    