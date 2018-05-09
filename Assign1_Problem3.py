#Problem Statement
#It is desired to calculate all integral powers of the number x = (√5.0 − 1.0) / 2.0 
#It turns out that the integral powers of x satisfy a recursive relation: x^n+1 = x^n-1 − x^n
#Show that the above recurrence relation	is unstable by calculating x16, x30,	x40 and x50 from the recurrence relation and comparing with the actual values obtained by using inbuilt function e.g., pow(a,b) in C.





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
        
