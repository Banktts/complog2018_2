data={}
lenN,lenM=[int(i) for i in input().strip().split()]
A=[int(i) for i in input().strip().split()][:lenN]
for i in range(lenN):
	for j in range(lenN):
		I=A[i]
		J=A[j]
		Sum=I+J
		if I+J not in data and i!=j:
			data[Sum]=set()
			data[Sum].add((I,J))
		elif i!=j and not (J,I) in data[Sum]:
			data[Sum].add((I,J))
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
				elif k[0]==j and k[1]==j:
					print("YES")
					st=False
					break
		if not st:
			break
	if st:
		print("NO")
