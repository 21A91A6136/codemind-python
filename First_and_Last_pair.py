a=int(input())
s=list(map(int,input().split()))
c=[]
for i in range(len(s)//2):
    print(s[i],s[len(s)-i-1],end=' ')
if(len(s)%2):
    print(s[len(s)//2],'0',end=' ')