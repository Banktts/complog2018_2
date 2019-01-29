x=input()
xl=sum(list(map(lambda i : int(i),x)))%2
print(x + "0") if xl==0 else print(x + "1")