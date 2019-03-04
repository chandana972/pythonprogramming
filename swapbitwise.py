j,k=map(int,input().split())
j = j ^ k
k = j ^ k
j = j ^ k
print(j,k)
