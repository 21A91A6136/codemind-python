n = int(input())
x = str(n)
op = [x]
for i in range(len(x)):
    if x[i] == "9": 
        z = x[:i] + "6" + x[1+i:]
    elif x[i] == "6":
        z = x[:i] + "9" + x[1+i:]
    op.append(z)
op.sort()
print(op[-1])