a=str(input())
l=[]
for i in a:
  if(i not in l):
    l.append(i)
print("".join(l))
