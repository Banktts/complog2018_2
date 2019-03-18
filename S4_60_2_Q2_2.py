data=""
Age=set()
distric=set()
dataHasAnalyse={}
for i in range(int(input().strip())):
    tm=input().strip()
    tmp=tm.split(",")
    Age.add(int(tmp[1]))
    distric.add(tmp[3])
    data+=tm
Age=list(Age)
distric=list(distric)
Com=input().strip().split(",")
if Com[0] == "P":
    for i in distric:
        n=data.count(i)
        if n not in dataHasAnalyse:
            dataHasAnalyse[n]=[i]
        else:
            dataHasAnalyse[n].append(i)
else:
     for i in Age:
        n=data.count(","+str(i)+",")
        if n not in dataHasAnalyse:
            dataHasAnalyse[n]=[i]
        else:
            dataHasAnalyse[n].append(i)
tmpKey=sorted(dataHasAnalyse.keys())
if Com[1]=="DSC":
    tmpKey=tmpKey[::-1]
if Com[2]=="ASC":
    for i in tmpKey:
        for j in sorted(dataHasAnalyse[i]):
            print(j,i)
else:
    for i in tmpKey:
        for j in sorted(dataHasAnalyse[i])[::-1]:
            print(j,i)
