a,b=map(int,input().split())
mat=[]
for i in range(a):
    l=list(map(int,input().strip().split()))
    mat.append(l)
for j in range(b):
    m=-100
    for i in range(a):
        if(m<=mat[i][j]):
            m=mat[i][j]
    print(m,end='
')
