def vowel(a):
    if a in'aeiouAEIOU':
        return 1
    else:
        return 0
def cons(a):
    if a in'aeiouAEIOU':
        return 0
    else:
        return 1
a=input().split()
c=0
for i in a:
    if (vowel(i[0]) and cons(i[-1])):
        c+=1
print(c)