n=int(input())
a=list(map(int,input().split()))
k=(n//2)
m=(n-1)
for i in range(m,k-1,-1):
    print(a[i],end=' ')
for i in range(0,k,1):
    print(a[i],end=' ')