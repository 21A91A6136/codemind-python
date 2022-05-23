x=int(input())
l=list(map(int,input().split()))
m=len(l)
c=0
for i in l:
    if i==0 or i==1:
        c+=1
if m==c:
    print("True")
else:
    print("False")