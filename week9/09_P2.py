def isSevenUp(x):
    return True if (x % 7 == 0 or "7" in str(x))and x != 0 else False
def nextSevenUp(x):
    return list(filter(lambda x: True if "7" in str(x) or x % 7 == 0 and x != 0 else False, range(x+1, x+15)))[0]
def prevSevenUp(x):
    return list(filter(lambda x: True if "7" in str(x) or x % 7 == 0 and x != 0 else False, range(x-1, x-15, -1)))[0]
f, x = input().strip().split()
x = int(x)
if f == 'isSevenUp':
    print(isSevenUp(x))
elif f == 'nextSevenUp':
    print(nextSevenUp(x))
elif f == 'prevSevenUp':
    print(prevSevenUp(x))
