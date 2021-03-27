#Неизменяемые типы данных не меняются в функциях
# Coplex numbers
x = 3
y = 4

z = complex(x,y)
print(z)

w = complex(y, x)

print(z + w)

# Strings
s = 'hello'
print(s[3])

#s[0] = 'H'#Так как строка неизменяемый тип данных так нельзя