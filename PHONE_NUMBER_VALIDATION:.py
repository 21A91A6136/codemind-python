x = int(input())
f =0
while x!=0:
    c = x%10
    f+=1
    x = x//10
if f==10:
    print("Valid")
else:
    print("Invalid")
    