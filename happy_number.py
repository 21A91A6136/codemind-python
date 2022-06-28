def hpy(n):
    x=n
    sum1=0
    while x>0:
        c=x%10
        sum1=(sum1+(c*c))
        x//=10
    return sum1
n=int(input())
hpy(n)
s=n
while s>9:
    s=hpy(s)
if  s==1 or s==7:
    print(True)
else:
    print(False)