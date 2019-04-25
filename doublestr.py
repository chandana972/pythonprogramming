a=input()
b=len(a)
c=int(b/2)
r=a[0:c]
s=a[c+1:b]
if r==s:
  print("YES",end="")
else:
  print("NO",end="")
