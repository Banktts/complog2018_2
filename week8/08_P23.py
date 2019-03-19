data={}
lenN,lenM=[int(i) for i in input().strip().split()]
A=[int(i) for i in input().strip().split()][:lenN]
for i in A:
	for j in A:
			if i+j not in data:
				data[i+j]=set()
				data[i+j].add((i,j))
			else:
				data[i+j].add((i,j))
M=[int(i) for i in input().strip().split()][:lenM]
for i in M:
	st=True
	for j in A:
		tmp=i-j
		if tmp in data:
			for k in data[tmp]:
				if j not in k:
					print("YES")
					st=False
					break
		if not st:
			break
	if st:
		print("NO") 
