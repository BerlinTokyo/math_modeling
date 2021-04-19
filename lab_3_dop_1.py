import numpy as np 
import random as rnd

#rnd .randint(0,100)

M=int(input())
N=int(input())
x=np.zeros((M, N))
A=np.zeros((M, N))

for i in range(0, M):
  for j in range(0, N):
    A[i, j]=rnd .randint(0,100)
    x[i, j]=rnd .randint(0,100)

print(A)
print(x)

E=np.zeros((M, N))
for i in range(0, M):
  for j in range(0, N):
    if A[i, j]>x[i, j]:
      E[i, j]=A[i, j]
    elif A[i, j]<x[i, j]:
      E[i, j]=x[i, j]
    else:
      E[i, j]=A[i, j]

print(E)