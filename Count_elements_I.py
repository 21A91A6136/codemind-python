a,b=map(int,input().split())
s=list(map(int,input().strip().split()))
d=list(map(int,input().strip().split()))
k=[]
for i in s:
  if i in d:
      k.append(i)
print(len(set(k)))
