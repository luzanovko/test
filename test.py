a, b = (int(i) for i in input().split())
s = 0
k = 0
for i in range(a, b+1):
  if i % 3 == 0:
    s +=i
    k +=1
print(s/k))