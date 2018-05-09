#Generalize the above program to input data points from a data file points.dat (a sample program to read data from a data file is given here ).
X = []
Y = []
f = open('points.dat','r')
for line in f : 
    t = line.split()
    X.append(float(t[0]))
    Y.append(float(t[1]))
f.close()
l = len(X)
x = float(input("Enter the value of x : ")) 
for i in range(l-1):
    if (X[i] <= x < X[i+1]) :
        y = ((x - X[i])/(X[i+1] - X[i]))*(Y[i+1]-Y[i]) + Y[i]
        print(y)

if (x == X[l-1]):
    print(Y[l-1])
if(x < X[0] or x > X[l-1]) :
    print("Out of range")
