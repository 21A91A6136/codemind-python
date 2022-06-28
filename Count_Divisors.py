a,b,c= map(int,input().split())
count=0
while a!=b+1:
    if a%c==0:
        count+=1
    a+=1    
print(count)