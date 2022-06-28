s=input()
s=list(s)


k=[]
for i in range(len(s)):
    c=0
    if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
        c+=1
        for j in range(i+1,len(s)):
            if(s[j]=="a" or s[j]=="e" or s[j]=="i" or s[j]=="o" or s[j]=="u"):
                c+=1
            else:
                
                break
        k.append(c)
    else:
        c=0
print(max(k))