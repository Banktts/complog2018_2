def GCD(x,y):
  if x>y and x%y==0:
    return y
  else:
    return GCD(y,x%y)
x,y=[int(i) for i in input().strip().split()]
print(GCD(x,y))
