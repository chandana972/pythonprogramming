y=input()
s=0
w=len(y)
for i in range(0,w):
  s=s+int(y[i])**w
print(s,end="")
