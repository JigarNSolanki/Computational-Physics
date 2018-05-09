import math
x = (math.sqrt(5.0) - 1.0 )/2.0 

def power(n):
    if n == 0 : 
        return 1
    elif n == 1 :
        return x
    else :
        a = (power(n-2))*(1-x)     
        return a

z = [16,30,40,50]    
print("From recursive function      From inbuilt function            error")
for i in range(4) :
        ya = power(z[i])
        yb = math.pow(x,z[i])
        print(ya,"   ",yb,"   ",(ya - yb)/yb)
        
