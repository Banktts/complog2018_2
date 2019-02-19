x=input().strip().split()
x=[int(i) for i in x]
n=len(x)
m=(n//2)
data=[]
data.append(x)
total=0
r=((n+1)//2)-1
for i in range(r):
		x=input().strip().split()
		x=[int(i) for i in x]
		data.append(x)
for i in range(r+1):
    for j in range(m-i,m+i+1):
        total+=data[i][j]
print(total)


