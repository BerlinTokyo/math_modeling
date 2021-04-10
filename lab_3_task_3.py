import numpy as np 

t = np.arange(0, 10, 1)

x0 = 0
y0 = 0
vx0 = 6
vy0 = 1
g = 9.8

x=x0+vx0*t
y=y0+vy0*t-(g*t**2)/2

print(t)
print(x)
print(y)

xy = np.zeros((len(t),3))
print(xy)

for i in range(0, 10):
  xy[i, 0] = t[i]
  xy[i, 1] = x[i]
  xy[i, 2] = y[i]
print(xy)


