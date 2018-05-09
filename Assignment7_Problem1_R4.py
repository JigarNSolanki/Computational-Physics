#link to problems: http://10.33.1.12/~comphy/ode.html
import math
def f(x):
    return 4*x*(1-x*x)
def E(x,v):
    return v**2/2 +(x**2-1)**2
    
h = 0.00061
X = [[1],[-1],[1]]
V = [[0.1],[0.1],[10]]

print("Using 4th order Runge-Kutta Method : ")
for j in range(1):
    Eo = E(X[j][0],V[j][0])
    for i in range(500):
        k1 = f(X[j][i])
        k2 = f(X[j][i] + h/2)
        k3 = f(X[j][i] + h/2)
        k4 = f(X[j][i] + h)
        V[j].append(V[j][i]+(k1+2*k2+2*k3+k4)*h/6)
        m1 = V[j][i]
        m2 = V[j][i] + h/2
        m3 = V[j][i] + h/2
        m4 = V[j][i] + h
        X[j].append(X[j][i]+(m1+2*m2+2*m3+m4)*h/6)
        #print X[j][i+1],V[j][i+1]
        Error=math.fabs((E(X[j][i],V[j][i])-Eo))*100/Eo
        if Error > 1:
            print("Error is more than 1%")
            break
        else:    
          print(Error)
    print(" ")
    
print("Step length for\nfirst condition 0.00061\nsecond condition 0.00065\nthird condition 0.00064")
