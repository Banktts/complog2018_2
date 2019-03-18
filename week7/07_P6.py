data=[]
row=int(input())
col=int(input())
for i in range(row):
	data.append(input().strip())
rowSa=[]
Rowdata=""
st=False
for i in range(len(data)):
	for j in range(len(data)):
		if data[i] == data[j] and i!=j:
			rowSa.append(i+1)
			rowSa.append(j+1)
			Rowdata=data[i]
			st=True
			break
	if st:
		break
for i in sorted(rowSa):
	print(i)
	print(Rowdata)
