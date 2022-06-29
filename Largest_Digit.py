a=int(input())
k=0
while(a):
    d=a%10
    if(k<d):
        k=d
    a//=10
print(k)