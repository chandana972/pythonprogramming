a,b=map(str,input().split())
l=[]
if(b in a):
  print(b)
else:
  for i in range(0,len(b)):
    for j in range(0,len(b)):
      if(a[i]==b[j]):
        l.append(a[i])
print("".join(l),end="")
