a=input().replace(' ','')
a=a.lower()
s=[]
for i in a:
    if i not in s:
        s.append(i)
d=0
for i in s:
    if(a.count(i)==1):
        d=1
        print(i)
        break
if(d==0):
    print('-1')