r,u=map(int,input().split())
l=[]
for n in range(r+1,u):
  t = n
  s = 0
  while t > 0:
    d = t % 10
    s+= d ** 3
    t //= 10
  if n == s:
    l.append(n)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end=" ")
