import math
x = float(input("Enter the value of x : "))
xo = x + 0.01
a = 4.0
n = 16
while n < 200 :
        x = a*x*(1-x)
        xo = a*xo*(1-xo)
        print(math.log(math.fabs(xo-x) / 0.01),"    ",n)
        n = n+1

