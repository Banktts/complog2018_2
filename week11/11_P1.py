import numpy as np
data1=[]
data2=[]
n=int(input())
for i in range(n):
  x=input().strip().split()
  data1.append(list(map(lambda i:float(i.strip()),x[1:])))
data1=np.array(data1)
for i in range(n):
  x=input().strip().split()
  data2.append(list(map(lambda x:float(x.strip()),x[1:])))
data2=np.array(data2)
newdata=data1*data2
for i in newdata.T:
  print(np.sum(i))
