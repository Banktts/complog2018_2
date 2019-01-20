import math
x=float(input())
SUM=0
k=0
term=10**-8
status = True
while status == True:
    term=((-1)**(k)*(x**(2*k)))/(math.factorial(2*k))
    if abs(term)>=10**(-8):
        k+=1
        SUM+=term
    else:
        status=False
print(SUM,k-1)

    