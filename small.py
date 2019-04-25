a,b=input().split()
a=int(a)
b=int(b)
l=list(str(a))
while b>0:
  b=b-1
  del(l[b])
r=(''.join(l))
print(r,end="")
