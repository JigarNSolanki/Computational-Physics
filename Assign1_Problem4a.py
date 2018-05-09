#Problem_Statement
#Consider the logistic map: xn+1 = A xn (1 − xn)
#where, xn is the nth iteration for 0 ≤ x ≤ 1. Here A is a constant. Vary the value of A from 0.89 to 3.995 in an interval of 0.0125 in each step. 
#(a) For each value of A, note the values of xn for 15 < n < 200, then make a plot of xn vs. A and see the bifurcation and chaos.
#(b) For A = 4.0, choose two points x and x' where, x' = x + 0.01 and iterate. Plot log(|xn − x'n| / 0.01) as a function of n. See if it is approaching a straight line.

x = float(input("Enter the value of x : "))

a = 0.89
while a <= 3.995 :
    n = 16
    while n < 200 :
        x = a*x*(1-x)
        print(a,x)
        n = n+1
    a = a + 0.0125
