X = [1.0,2.1,5.0]
Y = [8.0,20.6,13.7]
for i in range(3,5):
     X.append(X[i-3])
     Y.append(Y[i-3])
def P(x) :
     y = 0
     for i in range(3):
          yi = Y[i]*((x-X[i+1])*(x-X[i+2]))/((X[i]-X[i+1])*(X[i]-X[i+2]))
          y = y + yi
     return y
def L(x):    
    for i in range(2):
        if (X[i] <= x <= X[i+1]) : 
            y = ((x - X[i])/(X[i+1] - X[i]))*(Y[i+1]-Y[i]) + Y[i]
            return(y)
print("x         Polynomial fit         Linear fit           Difference ")
for i in range(11,50,2):
      j=i/10
      print(j,"     ",P(j),"     ",L(j),"    ",P(j)-L(j))
