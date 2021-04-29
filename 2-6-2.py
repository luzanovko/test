n = int(input())
b = [[0 for j in range(n)] for i in range(n)]
n1 = 0
n2 = 1
s = 'verh'
while n2 < n * n:
    if s == 'verh':
        for i in range(n1,n-1-n1):
            b[n1][i] = n2
            n2 += 1
        s = 'pravo'
    if s == 'pravo':
        for i in range(n1,n-1-n1):
            b[i][n-1-n1] = n2
            n2 += 1
        s = 'niz'
    if  s== 'niz':
        for j in range(n-1-n1,n1,-1):
            b[n-1-n1][j] = n2
            n2 += 1   
        s = 'levo'
    if s == 'levo':
        for i in range(n-1-n1,n1,-1):
            b[i][n1] = n2
            n2 += 1
        s='verh'
        n1 += 1
if n % 2 != 0:
     b[n //2 ][n //2] = n*n
for i in range(n):
    for j in range(n):
        print(b[i][j], end=' ')
    print()