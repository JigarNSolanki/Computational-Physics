#Given the three data points (x, y) = (1.0, 8.0), (2.1, 20.6) and (5.0, 13.7).
#write a program to return the value of y for any arbitrary x in the range [1.0, 5.0]. The program should exit if x is outside this range.
X = [1.0,2.1,5.0]
Y = [8.0,20.6,13.7]
x = float(input("Enter the value of x : ")) 

for i in range(2) :
    if (X[i] <= x <= X[i+1]) :
        y = ((x - X[i])/(X[i+1] - X[i]))*(Y[i+1]-Y[i]) + Y[i] 
        print(y) 
if(x < X[0] or x > X[2]) :
    print("Out of range")
