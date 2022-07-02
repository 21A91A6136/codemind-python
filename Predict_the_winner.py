n=int(input())
a=list(map(int,input().strip().split()))
x=0
y=0
for i in range(n):
    if(i<n//2):
       x+=a[i]
    else:
        y+=a[i]
if(abs(x-y)%4==0):
    print('X')
else:
    print("Y")