from functools import reduce
import numpy as np
def checker(n):
	tmp=np.zeros((n,n),int)
	for i in range(0 if n%2==1 else 1 ,n,2):
		np.fill_diagonal(tmp[n-i:n,:i],1)
		np.fill_diagonal(tmp[:i,n-i:n],1)
	return tmp
def collide(e,c):
	return np.array(list(filter(lambda i: np.sqrt((i[0]-e[0])**2+(i[1]-e[1])**2) <= i[2]+e[2] , c  )))
def matrix_chain_mult(M, order):
	tmp=M[order[0]]
	for i in range(1,len(order)):
		if i%2==1:
			tmp=tmp.dot(M[order[i]])
		else:
			tmp=M[order[i]].dot(tmp)
	return tmp
exec(input().strip()) # do not remove this line
