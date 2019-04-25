import math
a=input()
l=list(a)
m=[]
s=0
for x in range(0,len(l)):
  g=pow(int(l[x]),x)
  s=s+g
print(s,end="")
