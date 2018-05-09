#Link to problems: http://10.33.1.12/~comphy/integration2.html
import math
def f(x):
     return x*x*math.exp(-x*x)
def arc(x):
    return math.sqrt(1 + (math.cos(x))**2)     
F = [f,arc]
a = [-1,0]
b = [1,math.pi]

def intg(j):
    c = (b[j]-a[j])/2
    d = (b[j]+a[j])/2
    x1 = c*(-1/math.sqrt(3)) + d
    x2 = c*(1/math.sqrt(3)) + d

    I2 = c*F[j](x1)+c*F[j](x2)
    I3=c*((0.8889*F[j](c*0+d))+(0.5555*F[j](c*-0.7746+d))+(0.5555*F[j](c*0.7746+d)))
    I5=c*((0.5689*F[j](c*0+d))+(0.4786*F[j](c*-0.5385+d))+(0.4786*F[j](c*0.5385+d))+(0.2369*F[j](c*-0.9062+d))+(0.2369*F[j](c*0.9062+d))) 
    I = [I2,I3,I5]
    i = [2,3,5]
    for k in range(3):
        print("Using",i[k],"points : ",I[k])
    if j==1:
        s = 3.8202   
        print("Error")
        for k in range(3):
                print("Using",i[k],"points : ",math.fabs((I[k]-s)*100/s),"%")
     
for j in range(2):
    intg(j) 
    print(" ")
