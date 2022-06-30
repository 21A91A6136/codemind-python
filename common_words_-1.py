a=input()
b=input()
c=0
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
for i in a:
    if i in b:
        c+=1
print(c)