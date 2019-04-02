def knows(R,x,y):
  if x in R[y]:
    return False
  else:
    return True
def is_celeb(R,x):
  if R[x]-{x} != set():
    #print("1",x)
    return False
  for y in R:
    if  knows(R,x,y) and x!=y: 
      #print("2",x,y)
      return False
  #print("3",x)
  return True
    
def find_celeb(R):
  for x in sorted(R):
    if is_celeb(R,x):
      return x 
  return None 
def read_relations():
  R=dict()
  while True:
    d=input().split()
    if len(d) == 1 :break
    if d[0] not in R:
      R[d[0]]={d[1]}
    else:
      R[d[0]].add(d[1])
    if d[1] not in R:
      R[d[1]]=set()
  return R 
def main():
  R=read_relations()
  c=find_celeb(R)
  if c==None:
    print("Not Found")
  else:
    print(c)
exec(input().strip())
