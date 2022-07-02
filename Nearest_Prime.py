def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
h=int(input())
while(h):
    n=int(input())
    for i in range(1,n+1):
        if(prime(i)):
            a=i
    i=n+1
    while(1):
        if(prime(i)):
            b=i
            break
        i+=1
    x=abs(a-n)
    y=abs(b-n)
    if(x<y):
        print(a)
    elif(x==y):
        print(a)
    else:
        print(b)
    h-=1