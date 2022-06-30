a=list(map(str,input().split()))
c=0
s=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    s.append(c)
c=0
for i in s:
    if(max(s)==i):
        c+=1
print(c)