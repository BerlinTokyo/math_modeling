print('введите число а:')
a=float(input())
print('Введите число n:')
n=int(input())
def func(a,n):
  if n == 0:
    return 1
  else:
    return a*func(a,n-1)
print(func(a,n))