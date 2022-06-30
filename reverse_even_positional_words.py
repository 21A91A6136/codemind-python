a=list(map(str,input().split()))
for i in range(len(a)):
    s=[]
    if(i%2==0):
        s=a[i]
        print(s[::-1],end=' ')
    else:
        print(a[i],end=' ')