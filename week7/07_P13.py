dataID=[]
dataScore=[]
data=[]
Find=0
while True:
	x=input().strip().split()
	if len(x)==1:
		Find=int(x[0])	
		break
	else:
		dataID.append(int(x[0]))
		if float(x[1]) in dataScore:
			Index=0
			for i in range(len(data)):
				if float(x[1])==data[i][0]:
					Index=i
					break
			data[Index][1].append(int(x[0]))
		else:
			data.append([float(x[1]),[int(x[0])]])
		dataScore.append(float(x[1]))
if Find not in dataID:
	print("Not Found")
else:
	for i in data:
		Index=0
		Score=0
		if Find in i[1]:
			Index=sorted(i[1]).index(Find)
			Score=i[0]
			break
	IndexT=sorted(dataScore)[::-1].index(Score)+1+Index
	print(IndexT)
