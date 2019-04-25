k=input()
s=0
m=len(k)
for x in range(0,m):
  for y in range(0,x+1):
    s=s+int(k[y])
print(s,end="")
