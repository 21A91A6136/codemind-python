n=int(input())
c=0
for i in range(0,n+1):
    if(i*(i+1)==n):
        c+=1
if (c==1):
    print("YES")
else:
     print("NO")