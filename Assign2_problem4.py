import math
def f(x):
    return x**2 - math.exp(-x)
def dr(x):
    return 2*x + math.exp(-x)

x0 = 1
while math.fabs(f(x0)) > 0.000000001 :
    x = x0 - f(x0)/dr(x0)
    x0 = x
    print(x0)

print("The solution is : ",x0)