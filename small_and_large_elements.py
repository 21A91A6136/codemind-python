a=list(map(str,input().split()))
for i in a:
    print(min(i),end=' ')
    break
a=a[::-1]
for i in a:
    print(max(i))
    break