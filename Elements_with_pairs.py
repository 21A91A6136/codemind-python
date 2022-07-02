a=int(input())
s=list(map(int,input().split()))
print(*s,end=' ')
if(len(s)%2):
    print('0')