n=int(input())
temp=n
sum=0
for i in range(n):
    r=n%10
    sum=sum+r
    n=n//10
if temp%sum==n:
    print(True)
else:
    print(False)