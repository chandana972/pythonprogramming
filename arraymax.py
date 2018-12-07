dad=[]
bad=int(input(""))
for i in range(1,bad+1):
  c=int(input(" "))
  dad.append(c)
dad.sort()
print("",dad[bad-1])
