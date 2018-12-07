data= input(" ")
temp = 0
for c in data:
  if c.isspace() != True:
    temp = temp + 1
print(" ",temp)
