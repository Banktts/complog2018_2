from functools import reduce
def row_number(t,e):
  return list(filter(lambda x: e in t[x],range(len(t))))[0]
def flatten(t):
  return list(filter(lambda x: x!=0,reduce(lambda x,y:x+y ,t)))
def inversions(x):
  return len(list(filter(lambda x: x[0]>x[1] ,[[x[i],x[j]] for i in range(len(x)) for j in range(i,len(x))])))
def solvable(t):
  return True if len(t[0])%2!=0 and inversions(flatten(t))%2==0 else True if len(t[0])%2==0 and inversions(flatten(t))%2!=0 and row_number(t,0)%2==0 else True if len(t[0])%2==0 and inversions(flatten(t))%2==0 and row_number(t,0)%2!=0 else False
exec(input().strip())
