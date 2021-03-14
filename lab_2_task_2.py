print('Hello students')
print('Сompose a geometric progression')
print('Enter the first term of the geometric progression')
b1=int(input())
print('Enter the denominator of the progression')
q=int(input())
print('Indicate the number of members of the progression, an integer, no more than 10')
n=int(input())
l = []
for i in range(0, n):
  b1 *=q
  l.append(b1)
print(l)