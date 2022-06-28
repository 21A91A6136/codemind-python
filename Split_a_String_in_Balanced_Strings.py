a=input()
r=0
l=0
rl=0
for i in range (len(a)):
    if(a[i]=='R'):
        r+=1
    if(a[i]=='L'):
        l+=1
    if(l==r):
        rl+=1
print(rl)