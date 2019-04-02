import numpy as np
from math import e
data = np.array([[15,3.78],
                 [29,2.0],
                 [10,2.5],
                 [25,2.85],
                 [30,3.96]])
data2=np.array([0.2,0.5])
logit_pi =  np.sum(data2*data,axis=1 )-3.98
p_xi     = np.array(1/(1+e**((-1)*logit_pi)))
n = int(input())
if n<=0 or n>len(p_xi):
    print('Error')
elif p_xi[n-1]>0.5:
    print('True')
else:
    print('False')
