a =[int(i) for i in input().split()]
i = 1
if len(a) == 1 :
    print(a[0], end='')
else :
    print(a[1]+ a[-1])
    while i != len(a)-1 :
        print(a[i-1] + a[i + 1], end=' ')
        i += 1
    print(a[0] + a[-2])