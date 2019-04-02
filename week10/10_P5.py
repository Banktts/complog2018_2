def x(n):
  if n==0:
    return 0.01
  else:
    tmp=x(n-1)
    return 3*tmp*(1-tmp)
def M(n):
  if n<=1 :
    return 1 
  else:
    tmp=0
    for i in range(0,n-1):
      tmp+=M(i)*M(n-2-i)
    return M(n-1)+tmp
def D(m,n):
  if m<=0 or n<=0:
    return 1
  else:
    return D(m-1,n)+D(m-1,n-1)+D(m,n-1)
def S(n):
  if n<=2:
    return 1
  else:
    return int((1/n)*((6*n-9)*S(n-1)-(n-3)*S(n-2)))
def d(n):
  if n<1:
    return 1
  else:
    return n*d(n-1)+(-1)**n
exec(input().strip())
