def rev(n):
    r=s=0
    while(n):
        r=n%10
        s=s*10+r
        n//=10
    return s
def pn(n):
    r=s=0
    t=n
    while(n):
        r=n%10
        s=s*10+r
        n//=10
    if t==s:
        return 1
    else:
        return 0
def rp(n):
    r=rev(n)
    n+=r
    if pn(n):
        print(n)
        return 0
    else:
        return rp(n)
n=int(input())
rp(n)