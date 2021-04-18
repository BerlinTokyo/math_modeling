import numpy as np 
N=int(input())
M=int(input())
A=np.ndarray((N, M))

for i in range(0, N, 1):
  for j in range(0, M, 1):
    if i==0 and j==0:
      A[i, j] = np.sin(N*i+M*j)
    else:
      A[i, j] = np.sin(N*(i+1)+M*(j + 1))
print('Введите слолбик кторый хотите поменять местами:')
a=int(input())
print('Введите слолбик кторый хотите поменять местами:')
b=int(input())

m=np.zeros((N))
n=np.zeros((N))
print(A)
for i in range(0, N):
  m[i] = A[i,a]
  n=[i] = A[i,b]
for i in range(0, N):
  A[i, a] = n[i]
  A[i, b]=m[i]
print(A)

