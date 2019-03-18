dataWin,DataLose=set(),set()
for i in range(int(input().strip())):
	x,y=[i for i in input().strip().split()]
	if x not in dataWin:
		dataWin.add(x)
	if y not in DataLose:
		DataLose.add(y)
print(sorted(list(dataWin-DataLose)))
	
	
