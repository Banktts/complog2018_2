data,dataSet={},set()
dataComplete=[]
for i in open("address.txt"):
	x=i.replace("\n","").split()
	name=x[0]+" "+x[1]
	Tel=x[2]
	data[name]=Tel
	data[Tel]=name
	dataSet.add(name)
	dataSet.add(Tel)
while True:
	x=input().strip()
	if x=="":
		break
	if x in dataSet:
		dataComplete.append(data[x])
	else:
		dataComplete.append("Not Found")
[print(i) for i in dataComplete]
	
