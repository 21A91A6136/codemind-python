a=input().replace(' ','')
a=a.lower()
s=[]
for i in a:
    if i not in s:
        s.append(i)
print(''.join(sorted(s)))