data=[i.replace("\n","").strip() for i in open(input().strip())]
dataclear=[]
for i in data:
    if len(i.split(";"))==5:
        dataclear.append(i)
data=dataclear
Newdata=[]
for i in data:
    newdata=[]
    tmp=i.split(";")
    newdata.append(tmp[0])
    newdata.append(tmp[1]+" "+tmp[2])
    total=float(tmp[3])+float(tmp[4])
    newdata.append("A" if 80<=total<=100 else "B" if 70<=total<80 else "C" if 60<=total<70 else "D" if 50<=total<60 else "F")
    Newdata.append(newdata)
com=[]
while True:
    tmp=input().strip()
    if tmp == "-1":
        break
    else:
        com.append(tmp)
for i in com:
    st=True
    for j in Newdata:
        if i==j[0]:
            print(j)
            st=False
            break
    if st==True:
        print("Not Found")

