a=list(map(str,input().split()))
s=[]
for i in a:
    i=i[::-1]
    s.append(i)
print(*s[::-1])