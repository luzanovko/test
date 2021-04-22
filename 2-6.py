a = int(input())
if a == 1 or a == 0  :
  print(a)
else :
 b = []
 for i in range(a) :
   for j in range(i) :
     b += [i]
 for i in range(a) :
   print(b[i], end=' ')