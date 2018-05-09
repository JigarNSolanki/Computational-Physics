#link to problems: http://10.33.1.12/~comphy/ode.html

import math
q,m=-1.6E-19,9.1E-31
x,y,z=0,0,0
vx,vy,vz=1,1,1
B,Ey=1E-4,0
t,h=0,1E-9
k=h*q*B/m
l=h*q/m

T=2*math.pi*m/(-q*B)
print(t,x,y,z)

while(t<3*T):
    t=t+h
    x=x+h*vx
    y=y+h*vy
    z=z+h*vz
    vxd=vx
    vx=vx+k*vy
    vy=vy-k*vxd+l*Ey
    print(x,y,z)
