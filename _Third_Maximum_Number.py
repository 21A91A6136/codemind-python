a=int(input())
arr=list(map(int,input().split()))
arr.sort()
brr=[]
for i in arr:
    if i not in brr:
        brr.append(i)
if(len(brr)<3):
    print(max(brr))
else:
    print(brr[len(brr)-3])