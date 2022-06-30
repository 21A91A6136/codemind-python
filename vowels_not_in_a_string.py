a=input()
s=[]
for i in a:
    if i in 'aeiou':
        s.append(i)
f=0
for i in 'aeiou':
    if i not in s:
        f=1
        print(i,end=' ')
if(f==0):
    print('0')