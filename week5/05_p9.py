File=open(input(),"r")
FileStr=File.read()
lenghtFileStr=len(FileStr)-10
sc=[]
for i in range(lenghtFileStr):
	tmp=FileStr[i:i+10]
	st=True
	for j in tmp:
		if not(j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9"):
			st=False
	if st==True and tmp not in sc:
		sc.append(tmp)
[print(i) for i in sc]