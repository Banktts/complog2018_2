def h(n): 
    if n==0:
        return 0
    else:
        return 2*h(n-1)+1
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def J(n,k):
    if n==1:
        return 0
    else:
        return (J(n-1,k)+k)%n
def C(n):
    if n==0:
        return 1
    else:
        n=n-1
        tmp=0
        for i in range(n+1):
            tmp+=C(i)*C(n-i)
        return tmp
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n%2==0:
        n=n//2
        return (2*f(n-1)+f(n))*f(n)
    elif n%2==1:
        n=n//2+1
        return f(n)**2+f(n-1)**2
def F(n):
    if n==0:
        return 1
    else:
        return n-M(F(n-1))
def M(n):
    if n==0:
        return 0
    else:
        return n-F(M(n-1))
def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))
exec(input().strip()) # do not remove this line
