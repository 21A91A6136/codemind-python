import math
n=int(input())
a=list(map(int,input().split()))[:n]
l=[]
for i in range(0,len(a)):
    sq=int(math.sqrt(a[i]))
    if sq*sq==a[i]:
        l.append(a[i])
print(sum(l))