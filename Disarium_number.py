n=int(input())
sum=0
res=0
temp=n
while n:
    d=n%10
    sum+=1
    n=n//10
n=temp
while n:
    d=n%10
    res=res+(d**sum)
    n=n//10
    sum-=1
if(temp==res):
    print('True')
else:
    print('False')