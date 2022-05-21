def factsum(n):
    k=0
    for i in range(1,n):
        if(n%i==0):
            k=k+i;
    return k
n=int(input())
k=factsum(n)
if k>n:
    print("True")
else:
    print("False")
