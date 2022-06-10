n = int(input())
x = str(n)
o = [x]
for i in range(len(x)):
    if x[i] == "9": 
        z = x[:i] + "6" + x[1+i:]
    elif x[i] == "6":
        z = x[:i] + "9" + x[1+i:]
    o.append(z)
o.sort()
print(o[-1])
