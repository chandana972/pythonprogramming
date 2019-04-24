n=input()
l=[]
for i in n:
	if i.isdigit():
		l.append(i)
for j in range(0,len(l)):
	if j==len(l)-1:
		print(l[j],end="")
	else:
		print(l[j],end="")
