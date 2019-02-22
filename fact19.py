factorial = 1
num=int(input())
if num < 0:
   print("invalid")
elif num == 0:
   print("",1)
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(factorial,end="")
