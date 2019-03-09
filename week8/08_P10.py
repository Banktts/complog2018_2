data={}
dataId=[]
collected=[]
st=True
for i in range(int(input())):
    x=input().strip().split(": ")
    dataId.append(x[0])
    data[x[0].strip()]=set(x[1].strip().split(", "))
user=input().strip()
userdata=data[user]
for i in dataId:
    if i != user and userdata.intersection(data[i]):
        collected.append(i)
        st=False
if st:
    print("Not Found")
else:
    for i in collected:
        print(i)
