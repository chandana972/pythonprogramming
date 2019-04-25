a=int(input())
k=list(map(int,input().split()))
s=0
k.sort()
for i in range(0,a-1):
  s=s+k[i]
  if(s>k[i+1]):
    break
print(i+2,end="")
