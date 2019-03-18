data,n=[],[]
for i in range(int(input().strip())):
	x=int(input().strip())
	if x in data:
		n[data.index(x)]+=1
	else:
		data.append(x)
		n.append(1)
Max=max(n)
MaxT=0
MaxTlst=[]
for i in range(len(n)):
	if n[i] == Max:
		MaxT+=1
		MaxTlst.append(data[i])
MaxTlst=sorted(MaxTlst)
print(MaxTlst[0])
		
