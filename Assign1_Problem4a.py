x = float(input("Enter the value of x : "))

a = 0.89
while a <= 3.995 :
    n = 16
    while n < 200 :
        x = a*x*(1-x)
        print(a,"   ",x)
        n = n+1
    a = a + 0.0125