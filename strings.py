data1=input(" ")
data2=input(" ")
count1=0
count2=0
for i in data1:
      count1=count1+1
for j in data2:
      count2=count2+1
if(count1<count2):
      print(data2)
elif(count1==count2):
      print(data1)
else:
      print(data1)
