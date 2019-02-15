file=open(input(),"r")
data=[i.replace("\n","").strip() for i in file]
n=int(data[0].strip())
for i in range(1,n+1):
	j=[int(i) for i in data[i].split(" ")]
	SUM=sum(j[1:])
	print(j[0],"A" if 80<=SUM<=100 else "B+" if 75<=SUM<=79 else "B" if 70<=SUM<=74 else  "C+" if 65<=SUM<=69 else "C" if 60<=SUM<=64 else "D+" if 55<=SUM<=59 else "D" if 50<=SUM<=54 else "F")