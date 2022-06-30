a=input().lower().split()
b=input().lower().split()
s=[]
for i in a:
    if i in b:
        s.append(i)
for i in b:
    if i in s:
        print(i,end=' ')