import math
n,m=map(int,input().split())
k=n*m
r = math.sqrt(k)
if int(r + 0.5) ** 2 == k:
  print("yes",end="")
else:
  print("no",end="")
