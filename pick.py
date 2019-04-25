a=int(input())
l=[]
l=list(map(int,input().split()))
b=l[::2]
c=l[1::2]
d=l[1::3]
if(sum(b)>sum(c) and sum(b)>sum(d)):
  print(sum(b),end="")
elif(sum(d)>sum(b) and sum(d)>sum(c)):
  print(sum(d),end="")
else:
  print(sum(b),end="")
