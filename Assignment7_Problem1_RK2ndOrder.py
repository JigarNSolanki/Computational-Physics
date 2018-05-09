#link to problems: http://10.33.1.12/~comphy/ode.html

import math
def f(x):
    return 4*x*(1-x*x)
def E(x,v):
     return v**2/2 +(x**2-1)**2
    
h = 0.00086

V = [[0.1],[0.1],[10]]

print("Using 2nd order Runge-Kutta Method : ")
for j in range(1):
    V[j].append(V[j][0] + h*f(X[j][0]))
    X[j].append(X[j][0] + h*V[j][0])
    Eo = E(X[j][0],V[j][0])
    for i in range(1,250):
        V[j].append(V[j][i]+h*0.5*(f(X[j][i-1])+f(X[j][i-1]+h)))
        X[j].append(X[j][i]+h*0.5*(V[j][i]+V[j][i-1]))
        print(X[j][i],V[j][i])
        Error=math.fabs((E(X[j][i],V[j][i])-Eo))*100/Eo
        if Error > 1:
            print("Error is more than 1%")
            break
        else:    
          print(Error)
    print(" ")
    
print("Step length for\nfirst condition 0.00086\nsecond condition 0.00089\nthird condition 0.00065")
