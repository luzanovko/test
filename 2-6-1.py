n = 1
a = []
while n > 0:
  
  for i in range(n):
    row = input().split()
    if row != ['end']:
      for i in range(len(row)):
        row[i] = int(row[i])
      a.append(row)
    else :
      n = 0
print(a)