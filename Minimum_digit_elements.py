a=int(input())
s=list(map(int,input().split()))
g=[]
c=0
for i in s:
    i=list(str(i))
    #print(i)
    d=len(i)
    g.append(d)
for i in g:
    if(min(g)==i):
        c+=1
print(c)