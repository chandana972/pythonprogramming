a=input()
b=0
for x in a:
  b=int(x)+b
b=str(b)
m=b[::-1]
if(b==m):
  print("YES",end="")
else:
  print("NO",end="")
