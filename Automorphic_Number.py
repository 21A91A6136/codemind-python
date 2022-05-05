n=int(input())
h=len(str(n))
s=n**2
last=s%pow(10,h)
if last==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")