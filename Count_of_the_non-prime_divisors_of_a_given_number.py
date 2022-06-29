def prime(i):
    c=0
    d=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c!=2:
        d+=1
    return d
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(prime(i))
print(sum(l))