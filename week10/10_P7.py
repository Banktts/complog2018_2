def Cal(a,k,m):
  if k==0:
    return 1
  elif k%2==0:
    return (Cal(a,k//2,m)**2)%m
  else:
    return a*(Cal(a,k//2,m)**2)%m
a,k,m=[int(i) for i in input().strip().split()]
print(Cal(a,k,m))
