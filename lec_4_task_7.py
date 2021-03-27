def my_func(a, b):
    x = 3 * a - b
    return x

#tmp = my_func() #tmp - вызов функции и ничего не передает

def my_func(a=1, b=0): #По умолчанию
    x = 3 * a - b
    return x

print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))
print(my_func(b=3, a=9))

print('-------------')
#def my_func(a, b=0): #Сначала функция без аргументов
#    x = 3 * a - b
#    return x

# Так НЕЛЬЗЯ!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

def my_func(*args): #args - кортеж
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))
print(my_func(3, 4, 8))
def my_func(*args):
  for i in range(0, len(args)):
    b=i**2
    return b
    print(b)

print('-------------')
def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1=3, obj_2=4)) #Создали словарь обж_1 - ключи 3 - ответ
print(my_func(obj_1=3, obj_2=4, obj_3=8))
  