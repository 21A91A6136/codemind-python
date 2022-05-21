n=int(input())
h=len(str(n))
s=n**2
l=s%pow(10,h)
if l==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")