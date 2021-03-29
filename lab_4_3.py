import lec_3_constans #Импортировали константы
print('Привет давай посчитаем энергию, введи массу предмета в килограммах:') 
t=int(input())
print('Введи высоту броска в метрах:')
b=int(input())
print('Введи начальную скорость броска в метрах в секунду:')
p=int(input())
def mechanic_energy(m=t, H=b, V=p,):
  Ek=(m*(V**2))/2
  Ep=m*lec_3_constans.g*H
  x=Ek+Ep
  return x
print('Общая механическая энергия в джоулях:' ,mechanic_energy())