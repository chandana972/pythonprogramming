fact = 1
N=int(input())
if N < 0:
   print("invalid")
elif N == 0:
   print("",1)
else:
   for i in range(1,N + 1):
       fact = fact*i
   print(fact)
