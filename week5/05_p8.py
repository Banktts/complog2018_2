type=[0,0,0,0] #BE,SE,VE,ET
File=open(input().strip(),"r")
data=[i.replace("\n","") for i in File]
for i in data:
	tmp=i[0:3].strip()
	if tmp.upper() == "BE":
		type[0]+=1
	elif tmp.upper() == "SE":
		type[1]+=1
	elif tmp.upper() == "VE":
		type[2]+=1
	elif tmp.upper() == "ET":
		type[3]+=1
print(str(type[0])+" "+str(type[1])+" "+str(type[2])+" "+str(type[3])+" "+str(sum(type)))