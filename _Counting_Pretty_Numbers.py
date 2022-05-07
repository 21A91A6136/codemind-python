n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    c=0
    for i in range(x,y+1):
        r=i%10
        if(r==2 or r==3 or r==9):
            c+=1
    print(c)