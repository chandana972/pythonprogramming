k=int(input())
l=[]
r=sum(int(c) ** 2 for c in str(k))
l.append(r)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end="")

