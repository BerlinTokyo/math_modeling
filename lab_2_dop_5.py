a=int(input('Введите целое число:'))
b=[6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176,191561942608236107294793378084303638130997321548169216]
c=[]
while a:
  for i in b:
      if a>i:
        c.append(i)
      else:
        break
  break

print(c)
