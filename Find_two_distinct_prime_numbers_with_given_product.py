def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
             c+=1
    if(c==2):
        return 1
    else:
        return 0
a=int(input())
f=0
for i in range(1,a+1):
    if prime(i):
        for j in range(1,a+1):
            if prime(j):
                if(i*j==a):
                    x=i
                    y=j
                    f=1
                    break
if(f==0):
    print('-1')
else:
    print(y,x) 