data=[i.strip() for i in input().strip().split()]
com=input().strip()
for i in com:
    if i =="C":
        data1=data[:len(data)//2]
        data2=data[len(data)//2:]
        data=data2+data1
    elif i=="S":
        data1=data[:len(data)//2]
        data2=data[len(data)//2:]
        tmp=[]
        for i in range(len(data1)):
            tmp.append(data1[i])
            tmp.append(data2[i])
        data=tmp
for i in data:
    print(i,end=" ")
