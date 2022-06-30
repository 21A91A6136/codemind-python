a=input()
c=[]
d=[]
for i in range(len(a)):
    if(a[i].isalpha() or a[i].isdigit()):
        c.append(a[i])
    else:
        d.append(a[i])
c.sort()
j=0
k=0
for i in range(len(a)):
    if(a[i].isalpha() or a[i].isdigit()):
        print(c[j],end='')
        j+=1
    else:
        print(d[k],end='')
        k+=1