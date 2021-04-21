s = 'aaaabbcaa' #a4b2c1a2
i = 0
j = 0
k = ''
while i in range(len(s)-1):
    #print(s[i],s[i-1])
    if s[i] == s[i - 1] :
        j += 1 
        i += 1
    else :    
        print(s[i-1],j,i)
        print(s[i-1],s[i-j:i].count(s[i-1]))
        k = k + s[i-1] + str(s[i-j:i].count(s[i-1]))
        j += 0
        i += 1
print(k)