print('Привет, введи коэффициент а')
a=int(input())
print('Введи коэффициент b')
b=int(input())
print('Введи коэффициент c')
c=int(input())
print('Квадратное уравнение строится так')
print('(a*x**2*b*x+c)=0')
print('Найдем D, x1 и x2')
D=b**2-4*a*c
x1=(-b+(D)**0.5)/(2*a) 
x2=(-b-(D)**0.5)/(2*a)
print('D =',D)
if D==0:
  print('Имеется один корень', x1)
elif D>0:
  print('Мы вычислили корни')
  print('x1=', x1)
  print('x2=', x2)
else:
  print('D<0 => корней нет')

