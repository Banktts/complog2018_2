x=sorted([int(i) for i in input().strip().split()])
x1=set(x)
n=int(input())
cou=0
for i in x:
    tmp=n-i
    if tmp>0 and tmp in x1:
        cou+=1
print(cou//2)

