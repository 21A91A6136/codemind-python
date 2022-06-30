a,b=map(int,input().split())
s=list(map(int,input().split()))
g=[]
c=0
for i in s:
    if(i<0):
        i=abs(i)
    i=list(str(i))
    if(len(i)==b):
        c+=1
print(c)