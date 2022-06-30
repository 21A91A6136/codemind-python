a=input().replace(' ','')
a=a.lower()
s=[]
for i in a:
    if i not in s:
        s.append(i)
d=''
for i in s:
    if(a.count(i)==1):
        d+=i
print(len(sorted(d)))