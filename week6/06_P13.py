data=[i+1 for i in range(int(input().strip()))]
st=True
while st:
    x=input().strip().split()
    a,b=int(x[0]),int(x[1])
    if a==0 and b==0:
        st=False
    else:
        first=data.index(a)
        sec=data.index(b)
        data[first]=b
        data[sec]=a
print(data)