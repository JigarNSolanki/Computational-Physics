#Link to Problems: http://10.33.1.12/~comphy/integration2.html
import math
def f1(x) :
    return x
def f2(x) :
    return x*x
def f3(x) :
    return math.sin(x)
def f4(x) :
    return x*math.sin(x)

F = [f1,f2,f3,f4]
B = [1,1,math.pi,math.pi]
YA = [0.5,1/3,2 ,math.pi]
def trap(n,j) :
    s,a,b = 0,0,B[j]
    h = (b-a)/n
    while a < b:
        s = s + F[j](a)+F[j](a+h)
        a = a + h
    return s*h/2

def simp(n,j):
    s,a,b = 0,0,B[j]
    h = (b-a)/n
    for k in range(0,n,2) :
         s = s + F[j](a)+ 4*F[j](a+h)+F[j](a+2*h)
         a = a + 2*h
    return s*h/3     

print("Error(using trapazoidal) with n ")
for j in range(4):
    for i in range(10):
        n = pow(2,i+1)
        Yn = trap(n,j)
        print(n,"  ",math.fabs((Yn-YA[j]) / YA[j]))
    print(" ")

print(" ")
print("Error(using simpson) with n ")
for j in range(4):
    for i in range(10):
        n = pow(2,i+1)
        Yn = simp(n,j)
        print(n,"  ",math.fabs((Yn-YA[j])/YA[j]))
    print(" ")
