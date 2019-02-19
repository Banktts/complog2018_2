data=[i for i in input().strip()]
n=int(input().strip())
for i in range(n):
    com=input().strip().split()
    if com[0]== "in":
        data.insert(int(com[2]),com[1])
    elif com[0] == "out":
        data=data[:int(com[1])]+data[int(com[1])+1:]
    else:
        tmp1=data[int(com[1])]
        tmp2=data[int(com[2])]
        data[int(com[1])]=tmp2
        data[int(com[2])]=tmp1
    print("".join(data))