import numpy as np
def all_pair_distances(p):
	x = p[:,:1].reshape(1,len(p))[0]
	y = p[:,1:2].reshape(1,len(p))[0]
	X =np.array([x]) 
	Y =np.array([y]) 
	dX = X-X.T
	dY = Y-Y.T
	d = np.sqrt(dX**2+dY**2)
	return d
exec(input().strip()) # do not remove this line


 
