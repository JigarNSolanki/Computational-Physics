

import math
def f(x):
    return math.tan(x) - (2*math.sqrt((10.0/x)**2 - 1 )) / (2 - (10.0/x)**2) 

A = [2,5]
B = [3,6]
C = []
print("The soltuion for z are : ")
for i in range(2) : 
    a,b = A[i],B[i] 
    while math.fabs((b-a)/a) > 0.0001 :
        c = (a+b)/2
        if f(c)*f(b) < 0 :
            a = c
        else : 
            b = c
    C.append(c)       
    print(i+1,":",c)

a,b = -1,1.1
while math.fabs((b-a)) > 0.0001 :
    c = (a+b)/2
    if f(c)*f(b) < 0 :
        a = c
    elif f(c)*f(a) < 0 :
        b = c
C.append(c)            
print("3 : ",c)

print("Corresponding allowed energy : ")
for i in range(3):
    c = C[i]
    e = c**2 - 10.0**2
    print(i+1,": ",e)
