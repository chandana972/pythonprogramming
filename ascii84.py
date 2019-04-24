ch=input()
l=[]
for i in range(0,1):
  k=ord(ch)
  l.append(k)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end=" ")
