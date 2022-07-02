def prime(a):
    c=0
    if(a==1):
        return 1
    for i in range(1,a+1):
        if(a%i==0):
            c+=1
    if(c>2):
        return 1
    else:
        return 0
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if(prime(i)):
            c+=1
print(c)