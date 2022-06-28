l=list(map(int,input().split()))
n=len(l)
max1=0
max2=0
for i in range(0,n):
    if(max1<l[i]):
        max1=l[i]
        a=i
for i in range(0,n):
    if(max2<l[i] and i!=a):
        max2=l[i]
max1-=1
max2-=1
print(max1*max2)