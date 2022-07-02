n=int(input())
a=list(map(int,input().strip().split()))
c=0
for i in range(n):
    dc=0
    while(a[i]):
        d=a[i]%10
        dc+=1
        a[i]//=10
    if(dc%2==0):
        c+=1
print(c)