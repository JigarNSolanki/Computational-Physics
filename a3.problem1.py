X = [1.0,2.1,5.0]
Y = [8.0,20.6,13.7]
x = float(input("Enter the value of x : ")) 

for i in range(2) :
    if (X[i] <= x <= X[i+1]) :
        y = ((x - X[i])/(X[i+1] - X[i]))*(Y[i+1]-Y[i]) + Y[i] 
        print(y) 
if(x < X[0] or x > X[2]) :
    print("Out of range")