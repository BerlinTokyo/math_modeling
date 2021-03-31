
print('Введи n:')
n=int(input())
def fib(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  elif n==3:
    return 1
  else:
    return fib(n-1)+fib(n-2)
print(fib(n))


  
