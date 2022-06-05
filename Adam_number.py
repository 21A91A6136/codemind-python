z=int(input())
r=0
rev=0
n=z
p=n*n
while n:
    m=n%10
    r=(r*10)+m
    n=n//10
c=r*r
while c:
    a=c%10
    rev=(rev*10)+a
    c=c//10
if p==rev:
    print("True")
else:
    print("False")