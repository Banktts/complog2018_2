dicStation={}
lastStation=""
stationCanConnected=[]
while True:
	x=input().strip().split()
	if len(x)==1:
		lastStation=x[0]
		break
	else:
		if x[0] in dicStation.keys() and x[1] not in dicStation[x[0]]:
			dicStation[x[0]].append(x[1])
		else:
			dicStation[x[0]]=[x[1]]
		if x[1] in dicStation.keys() and x[0] not in dicStation[x[1]]:
			dicStation[x[1]].append(x[0])
		else:
			dicStation[x[1]]=[x[0]]

if lastStation in dicStation.keys():
    tmp=dicStation[lastStation]
    stationCanConnected+=tmp
    for i in tmp:
        for j in dicStation[i]:
            if j not in stationCanConnected:
                stationCanConnected.append(j)
else:
    stationCanConnected+=[lastStation]
new=sorted(stationCanConnected)
[print(i) for i in new]
