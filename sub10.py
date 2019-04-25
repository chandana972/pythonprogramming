e,f=input().split()
j=input().split()
k=input().split()
j.sort()
k.sort()
s1=''.join(j)
s2=''.join(k)
if(s2 in s1):
  print("YES",end="")
else:
  print("NO",end="")
