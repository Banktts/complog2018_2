file=input().strip()
n=int(input())
pre=input()
suf=input()
data=open(file,"r")
dataFile=""
m=0
for line in data:
	dataFile+=line
i=0
while i < len(dataFile)-len(suf):
	if dataFile[i:i+len(pre)].lower()==pre.lower() and m<n:
		dataFile=dataFile[:i]+suf+dataFile[i+len(pre):]
		m+=1
		i+=len(suf)-1
	i+=1
print(dataFile)