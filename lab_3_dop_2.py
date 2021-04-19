import numpy as np 
import random as rnd 


A=np.zeros((5))
for i in range(0,4):
  A[i]=rnd.randint(0,113)
print(A)

i=int(input())
A[i]=13

if i==0:
  A[4]=A[3]
  A[3]=A[2]
  A[2]=A[1]
  A[1]=A[0]  
elif i==1:
  A[4]=A[3]
  A[3]=A[2]
  A[2]=A[1]
elif i==2:
  A[4]=A[3]
  A[3]=A[2]
elif i==3:
  A[4]=A[3]
else:
  A[4]=A[i]




print(A)
