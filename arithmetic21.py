N,A,D=map(int,input().split())
l=[]
sum1=((1/2)*N)
char=((2*A)+((N-1)*D))
r=char*sum1
l.append(r)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(int(l[p]),end="")
