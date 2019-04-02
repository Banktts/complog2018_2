def sumlist(x):
  if x==[]:
    return 0
  i=x.pop()
  if isinstance(i,int):
    return sumlist(x)+i
  else:
    return sumlist(x)+sumlist(i)
print(sumlist(eval(input().strip())))
