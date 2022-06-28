n=int(input())
l=[]
c=0
for i in range(n):
    
    l.append(int(input()))
w=int(input())
for i in l:
    if i>w:
        c+=2
    elif i<=w:
        c+=1
print(c)