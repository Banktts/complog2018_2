dataR={}
dataT={}
dataT1=[]
dataT2=[]
dataM=[]
while True:
    In=input().strip()
    if In=="done":
        break
    In=In.split()
    dataR[In[0]]=In[1:]
    for i in In[1:]:
        dataM.append(tuple([In[0],i]))
        if i not in dataT:
            dataT[i]={In[0]}
            dataT1.append(i)
            dataT2.append(1)
        else:
            dataT[i].add(In[0])
            dataT2[dataT1.index(i)]+=1
Com=[i.strip() for i in input().strip().split()]
if Com[0]=="R":
    for i in sorted(dataR.keys()):
        print(i,len(dataR[i]))
elif Com[0]=="T":
    Max=max(dataT2)
    tmp=[]
    for i in range(len(dataT2)):
        if Max==dataT2[i]:
            tmp.append(dataT1[i])
    tmp=sorted(tmp)
    [print(i) for i in tmp]
elif Com[0]=="C":
    if Com[1] in dataT and Com[2] in dataT:
        tmp=dataT[Com[1]].intersection(dataT[Com[2]])
        if tmp == set():
            print("None")
        else:
            tmp=sorted(list(tmp))
            [print(i) for i in tmp]
    else:
        print("None")
elif Com[0]=="M":
    lst=[]
    for i in dataM:
        if i[::-1] in dataM:
            lst.append(i)
    if lst!=[]:
        [print(i) for i in sorted(lst)]
    else:
        print("None")



