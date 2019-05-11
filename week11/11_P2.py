import numpy as np
data=[]
for i in range(int(input())):
  x=input()
  if x[0] in "0123456789":
    data.append( list(map(lambda i:float(i), x.split(",")[1:])) )
for i in data:
  print(np.sum(i))
