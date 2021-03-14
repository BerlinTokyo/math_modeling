print('Hello friend, write the number')
x=int(input())
l=[]
if x==1:
  e=(1)
  l.append(e)
  print(l)
elif x==2:
  print('[1, 1]')
else:
  for i in range(1, x+1):
    b=(((1+5**(1/2))/2)**int(i)-((1-5**(1/2))/2)**int(i))/5**(1/2)
    l.append(int(b))
  print(l)





