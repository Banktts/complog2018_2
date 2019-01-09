'''
lst=list(map(lambda x: int(x),input().split(" ")))
p=sum(lst)/2
print((p*(p-lst[0])*(p-lst[1])*(p-lst[2]))**(1/2))
'''
######simple code below
INPUT=input().split(" ")
a=int(INPUT[0])
b=int(INPUT[1])
c=int(INPUT[2])
p=(a+b+c)/2
Area=((p*(p-a)*(p-b)*(p-c))**(1/2))
print(Area)