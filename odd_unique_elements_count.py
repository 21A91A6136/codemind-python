n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if i%2!=0 and i not in b:
        b+=[i]
        c+=1
print(c)