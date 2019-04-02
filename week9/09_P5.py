def function1():
    sum = 0
    for i in range(10):
        sum += i
    return sum
def function2(n): 
    i= 2
    if n == 1:
        return False
    while i <= n**0.5:
        if n%i == 0:
            return False
        i += 1
    return True
def function3(n):
    for i in range(1,n):
        if function2(i):
            print(i)
def function4(x,y):
    match = 0
    notmatch = ''
    for i in x:
        if i == y:
            match += 1
        else:
            notmatch += i
    return [match,notmatch]
Com=input()
if Com != "function1":
    if Com == "function4":
        x,y=input().strip().split()
        exec("print("+str(Com)+"("+"\""+x+"\""+","+"\""+y+"\""+"))" )
    elif Com == "function3":
        x=input().strip()
        exec(str(Com)+"("+x+")" )
    else:
        x=input().strip()
        exec("print("+str(Com)+"("+x+"))" )
else:
    exec("print("+str(Com)+"""())""" )
