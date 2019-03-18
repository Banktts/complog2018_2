dataIn,data=set(),{}
dataInlst,dataLst=[],[]
for i in range(int(input().strip())):
	x=input().strip().split()[1]
	if x[:2] in dataIn:
		data[x[:2]].append(x)
		dataLst[dataInlst.index(x[:2])]+=1
	else:
		dataIn.add(x[:2])
		data[x[:2]]=[x]
		dataLst.append(1)
		dataInlst.append(x[:2])
Max=max(dataLst)
Maxt=0
Maxtt=[]
for i in range(len(dataLst)):
	if dataLst[i] == Max:
		Maxt+=1
		Maxtt.append(i)
if Maxt>1:
	MaxWord=[]
	for i in Maxtt:
		MaxWord.append(dataInlst[i])
	MaxWord=sorted(MaxWord)[0]
	word=data[MaxWord]
	print(MaxWord)
	print(Max)
	[print(i) for i in word]
else:
	MaxWord=dataInlst[dataLst.index(Max)]
	word=data[MaxWord]
	print(MaxWord)
	print(Max)
	[print(i) for i in word]
