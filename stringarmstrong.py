data=str(input(""))
data=data.casefold()
revdata=reversed(data)
if list(data)==list(revdata):
  print("yes")
else:
  print("no")
