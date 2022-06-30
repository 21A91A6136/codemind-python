a=input()
n=input()
f=0
for i in range(len(a)):
    if(a[i]==n):
        f=1
        print(True)
        print(i)
        break
if(f==0):
    print(False)