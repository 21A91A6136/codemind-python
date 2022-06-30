n=int(input())
a=list(map(int,input().split()))
b=[]
sum=0
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    sum+=i
print(sum)