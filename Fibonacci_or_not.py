n=int(input())
c=0
n1=0
n2=1
if n==0 or n==1:
    print("True")
else:
    while c<n:
        c=n1+n2
        n1=n2
        n2=c
    if(c==n):
        print("True")
    else:
        print("False")