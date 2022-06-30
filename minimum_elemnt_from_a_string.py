a=list(map(str,input().split()))
a=a[::-1]
for i in a:
    c=min(i)
    if c and c.lower() in i:
        print(c.lower())
        break
    else:
        print(c)