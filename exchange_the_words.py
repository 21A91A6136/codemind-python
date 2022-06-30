a=list(map(str,input().split()))
s=[]
for i in a:
    s.append(i)
print(*s[::-1])