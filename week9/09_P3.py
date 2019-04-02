def nextEven(f):
    return list(filter(lambda x:x%2==0,range(int(f)+1,int(f)+3)))[0]
def nextOdd(f):
    return list(filter(lambda x:x%2!=0,range(int(f)+1,int(f)+3)))[0]
while True:
    x = float(input())
    if x < 0:
        break
    even = nextEven(x)
    odd = nextOdd(x)
    print( (even, odd) )