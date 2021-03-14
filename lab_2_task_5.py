print('Hello, Enter two integers')
a=int(input())
b=int(input())
if a%b==0:
  print("Первое число делится на второе")
  print(a//b)
elif b==0:
  print('Ошибка, делитель равен 0')
else:
  print("Первое число не делится на второе")
  print('Целая часть')
  print(a//b)
  print('Остаток')
  print(a%b)
print('The end')


