a=int(input())
s=list(map(int,input().split()))
c=[]
for i in s:
    if i not in c:
        c.append(i)
h=[]
for i in c:
    h.append(i)
    h.append(s.count(i))
print(*h)