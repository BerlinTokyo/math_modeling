import numpy as np 
h=100
B=30
a=np.pi/3
g=9.8
x=(g*h*np.tan(B)*np.tan(B))
c=(2*np.cos(a)*np.cos(a)*(1-np.tan(B)*np.tan(a)))
v=(x/c)**0.5
print(v)
T=200
E=300
k=1.380649*(10**23)
e=2.71828
hh= 6.62607015*(10**34)
N=(2/(np.pi)**0.5)*(hh/((k*T)**3/2))*(e**(-E/k*T))*(e**(T/2))
print(N)