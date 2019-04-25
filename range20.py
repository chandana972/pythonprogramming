a,b=input().split()
a=int(a)
b=int(b)
l=[]
h=0
for i in range(a,b+1):
  m=list(bin(i))
  del m[1]
  m=map(int,m)
  l.append(sum(m))
for i in l:
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
      h+=1
print(h,end="")
