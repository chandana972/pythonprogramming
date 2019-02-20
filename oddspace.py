x,y=map(int,raw_input().split())
l=[]
for i in range(x,y+1):
    if(i%2!=0):
        l.append(i)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end=(""))
  else:
    print(l[p],end=" ")
