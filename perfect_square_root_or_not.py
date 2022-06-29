from math import sqrt
n=int(input())
def solve(n):
   sq_root = int(sqrt(n))
   return (sq_root*sq_root) == n
print (solve(n))