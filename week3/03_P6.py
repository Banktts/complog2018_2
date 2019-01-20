lst=input().split(" ")
N,f=lst[0],lst[1]
S=0
for i in range(int(N)):
    x=input().strip()
    if x == f:
        S+=1
print(S)