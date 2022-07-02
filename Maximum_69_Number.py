a=int(input())
s=list(str(a))
g=0
for i in range(len(s)):
    if(s[i]=='6'):
        s[i]='9'
        break
    else:
        continue
f=''.join(s)
print(f)