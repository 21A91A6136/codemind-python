a,b=map(int,input().split())
s=list(map(int,input().split()))
l=list(map(int,input().split()))
s=set(s)
l=set(l)
c=0
for i in s :
    if i not in l:
        c+=1
for i in l:
    if i not in s:
        c+=1
print(c)