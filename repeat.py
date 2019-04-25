a=int(input())
b=input().split()
w=len(b)
for i in range(0,w):
  q=b.count(b[i])
  if(q<2):
    print(b[i],end="")
