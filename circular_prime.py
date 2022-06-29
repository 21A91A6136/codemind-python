n=int(input())
count=0
rev=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    fcount=0
    for j in range(1,rev+1):
        if(rev%j==0):
            fcount+=1
    if(fcount==2):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")