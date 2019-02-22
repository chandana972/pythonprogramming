m=int(input())
l=[]
for i in range(1,6):
  k=i*m
  l.append(k)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end=" ")
