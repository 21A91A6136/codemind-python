n = input()
s=0
v=0
m=0
a=0
i=0
while i<len(n):
    if (n[i]=='A' or n[i]=='I' or n[i]=='O' or n[i]=='U' or n[i]=='E' or n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
        s+=1
    elif( n[i]>='0' and n[i]<='9'):
        v+=1
    elif( n[i] == ' '):
        m+=1
    else:
        a+=1
    i+=1
print("Vowels: %d"%s)
print("Consonants: %d"%a)
print("Digits: %d"%v)
print("White spaces: %d"%m)