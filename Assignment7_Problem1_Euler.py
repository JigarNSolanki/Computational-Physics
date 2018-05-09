#link to problems: http://10.33.1.12/~comphy/ode.html
import numpy as np
import matplotlib.pyplot as plt
import math 

def f(x):
    return 4*x*(1-x*x)
def E(x,v):
    return v**2/2 +(x**2-1)**2    

h = 0.015
X = [[1],[-1],[1]]
V = [[0.1],[0.1],[10]]

#print("Using Euler's Method : ")
for j in range(1,2):
    Eo = E(X[j][0],V[j][0])
    for i in range(1000):
        V[j].append(V[j][i]+h*f(X[j][i]))
        X[j].append(X[j][i] + h*V[j][i])
        #print(X[j][i],V[j][i])
        #Error=math.fabs((E(X[j][i],V[j][i])-Eo))*100/Eo
        #if Error > 1:
            #print("Error is more than 1%")
            #break
        #else:    
         # print(Error)  
        
        #plt.scatter(X[1],V[1])
 
    #print("  ")
    
#print("Step length for\nfirst condition 0.0015\nsecond condition 0.0016\nthird condition 0.00062")


