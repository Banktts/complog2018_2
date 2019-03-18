data=[set([i.strip() for i in input().strip().split()]) for i in range(int(input().strip()))]
if data==[]:
	print("0")
	print("0")
else:
	Union=data[0]
	Intersection=data[0]
	for i in range(1,len(data)):
		Union=Union.union(data[i])
		Intersection=Intersection.intersection(data[i])
	print(len(Union))
	print(len(Intersection))
