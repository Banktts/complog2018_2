data=[]
dataProduct=[]
for i in open("inventory.txt"):
	line=i.replace("\n","").strip().split(";")
	line=line[:2]+[int(line[2])]
	dataProduct.append(line[0])
	data.append(line)
while True:
	In=input().strip().split()
	if In[0] == "Q":
		print("Bye!")
		break
	elif In[0] == "A":
		if In[1] in dataProduct:
			print("Duplicate product code.")
		else:
			In=In[1:3]+[int(In[3])]
			data.append(In)
			dataProduct.append(In[0])
			print(In)
	elif In[1] not in dataProduct:
		print("Product code does not exist.")
	elif In[0]=="T":
		data[dataProduct.index(In[1])][2]+=int(In[2])
		print(data[dataProduct.index(In[1])])
	elif In[0] == "U":
		data[dataProduct.index(In[1])][2]=int(In[2])
		print(data[dataProduct.index(In[1])])
	elif In[0] == "D":
		Index=dataProduct.index(In[1])
		print(In[1]+" "+"deleted")
		data.pop(Index)
		dataProduct.pop(Index)

