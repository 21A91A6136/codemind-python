n=int(input())
for i in range(n+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    if(c==2):
        a=i
i=n
while(1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    i+=1
    if(c==2):
        b=j
        break
x=abs(n-a)
y=abs(n-b)
if(x<y):
    print(x)
else:
    print(y)