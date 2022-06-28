n=int(input())
for i in range(n):
    x=input()
    a=x[::-1]
    if x==a:
        if len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
