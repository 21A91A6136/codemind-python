x = input()
v = []
for i in x:
    if i.isdigit():
        v.append(int(i))
print(sum(v))