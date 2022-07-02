n=int(input())
a=list(map(int,input().strip().split()))
os=0
es=0
for i in range(n):
    if(i%2):
        os+=a[i]
    else:
        es+=a[i]
if(os-es==0):
    print('YES')
else:
    print('NO')