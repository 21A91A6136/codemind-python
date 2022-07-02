a=int(input())
s=list(map(int,input().split()))
c=[]
for i in s:
    if i&1!=0 and i not in c:
        c.append(i)
print(len(c))