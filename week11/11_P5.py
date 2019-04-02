import numpy as np
def read_square_matrix():
	d = [int(e) for e in input().split()]
	m = [d]
	for k in range(len(d)-1):
		m.append([int(e) for e in input().split()])
	return np.array(m)
def min_in_each_row(m):
	return np.min(m,axis=1)
def max_in_each_column(m):
	return np.max(m,axis=0)
def diff_of_sums_of_two_diags(m):
	return abs(np.sum(m.diagonal())-np.sum(m[::-1].diagonal()))
def halve(m):
	return np.array([[np.sum(m[ i :i+2,j:j+2]) for j in range(0,len(m),2)  ]for i in range(0,len(m),2)])
exec(input().strip()) 
