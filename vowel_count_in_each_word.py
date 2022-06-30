a=list(map(str,input().split()))
c=0
s=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    s.append(c)
print(*s)