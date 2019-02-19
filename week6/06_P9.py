comlst=[]
data=[]
while True:
    com = input().strip()
    comlst.append(com)
    if com=="end":
        break
for com in comlst:
    if com=="list":
        print(data)
    elif com=="shelf":
        if len(data)==0:
            print("no book")
        else:
            print(data[-1])
            data.pop()
    elif com=="top":
        if len(data)==0:
            print("no book")
        else:
            print(data[-1])
    elif com=="end":
        break  
    else:
        com=com.replace("return","").strip()
        data.append(com)
        print(len(data))