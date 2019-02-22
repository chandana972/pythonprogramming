m,n=map(int,input().split())
l=[]
for val in range(m, n ):   
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
          l.append(val)
for p in range(0,len(l)) :
  if(p==len(l)-1):
    print(l[p],end="") 
  else:
    print(l[p],end=" ")        


