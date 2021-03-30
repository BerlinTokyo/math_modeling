import lec_3_constans
i=2
while i>1:
  print('Привет, площадь какой фигуры тебе хочется найти? 1 - круг, 2 - прямоуголник, 3 - треугольник')
  x=int(input())
  if x==1 or x==2 or x==3:
    i = 0
  else:
    print('Не распозноваемый ответ')
if x==1:
  print('Круг? Неплохой выбор. Введи радиус:')
  rad=int(input())
  Sk=(rad**2)*lec_3_constans.Pi 
  print('Площадь твоего круга:' ,Sk)
elif x==2:
  print('Прямоугольник тоже сойдет. Введи первую сторону:')
  per=int(input())
  print('Введи вторую сторону:')
  vtor=int(input())
  Spr=per*vtor
  print('площадь твоего прямоугольника:' ,Spr)
elif x==3:
  print('Треугольник это круто. Введи первую сторону:')
  van=int(input())
  print('Введи значение второй стороны треугольника')
  ty=int(input())
  print('Введи значение третьей стороны треугольника')
  fri=int(input())
  print('Введи значение четвертой стороны треугольника')
  fo=int(input())
  if fo!=0:
    print('Ошибка, треугольник имеет только три стороны)')
    print('Продолжим')
  else:
    print('Неплохо)))')
    print('Продолжим')
  if van+ty>fri and van+fri>ty and ty+fri>van:
    peri=(van+ty+fri)/2
    print('Такой треугольник существует.')
    if van==ty or van==fri or ty==fri:
      S12=(peri*(peri-van)*(peri-ty)*(peri-fri))**0.5
      print('Треугольник равнобедренный. его площадь:' ,S12)
    elif van==ty and ty==fri:
      S11=(peri*(peri-van)*(peri-ty)*(peri-fri))**0.5
      print('Треугольник равносторонний, ео площадь:' ,S11)
    else:
      S13=(peri*(peri-van)*(peri-ty)*(peri-fri))**0.5
      print('Треугольник разносторонний, его площадь:' ,S13)
  else:
   print('Такого треугольника не существует')


