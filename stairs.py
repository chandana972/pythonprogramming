a=int(input())
s=input().split()
s=list(map(int,s))
k=[]
for i in range(1,a):
  m=0
  for j in range(i):
    if(s[i]>s[j]):
      m=m+s[j]
  k.append(m)
print(sum(k),end="")
