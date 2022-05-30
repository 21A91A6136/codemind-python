def add_digits(n):
    while n>=10:
        t=0
        while n>0:
            t=t+n%10
            n//=10
        n=t
    return n
n=int(input())
if(add_digits(n)>=10):
    add_digits(n)
else:
    print(add_digits(n))