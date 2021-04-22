a = [int(i) for i in input().split()]
b = []
for i in a :
  if a.count(i) >=2 and b.count(i) == 0 :
    b.append(i)
for i in b :
  print(i, end=' ')