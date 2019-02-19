n=int(input().strip())
data1=[]
data2=[]
for i in range(n):
    data2.append(int(input().strip()))
    data1.append(i+1)
tmp=1
print(tmp,end=" ")
for i in range(n-1):
    tmp=data2[data1.index(tmp)]
    print(tmp,end=" ")