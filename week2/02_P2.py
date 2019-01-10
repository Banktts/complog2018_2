#print(sorted([int(input()) for i in range 5 ])[2])
################
def SORT(e):
	n=len(e)
	for i in range(n-1):
		for j in range(n-1):
			if e[j]>e[j+1]:
				e[j+1],e[j]=e[j],e[j+1]
	if e[0]>e[-1]:
		e[-1],e[0]=e[0],e[-1]		
	return e
LS=[]
for i in range(5):
	x=int(input())
	LS.append(x)
print(SORT(LS)[2])