import collections
a=list(input().replace(' ',''))
d=collections.Counter(a)
d=sorted(d)
print(d[0],a.count(d[0]),d[-1],a.count(d[-1]))