import numpy as np
n=int(input())
x=np.array([[int(i.strip()) for i in input().strip().split()] for i in range(n)])
for M in range(n):
	j,i=np.where(x==1)
	for I in range(len(j)):
		tmp=np.where(j==i[I])
		for J in tmp[0]:
			if j[I] != i[J] and x[j[I],i[J]] ==0:
				x[j[I],i[J]]+=1	
list(map(lambda i: print(" ".join(map(str,i))),x))


	
