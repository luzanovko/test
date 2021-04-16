a = int(input())
b = int(input())
c = int(input())
ost=0
max =a
min= b 
if b> max : 
    max = b
elif c > max : 
    max = c 
if b < min : 
    min= b
elif c < min : 
    min = c 
ost = (a+b+c)-min-max
print(max)
print(min)
print(ost)