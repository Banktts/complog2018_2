x=input().split(" ")
STR=x[0]
NUM=x[1]
strTrue=""
val=0
for i in range(len(STR)):
	if ((ord(STR[i]) >= 65 and ord(STR[i]) <= 90) or (ord(STR[i]) >= 97 and ord(STR[i]) <= 122)):
		strTrue=strTrue+STR[i]
for i in range(len(NUM)):
	if (ord(NUM[i]) >= 47 and ord(NUM[i]) <= 57):
		val+=int(NUM[i])
print(strTrue[0].upper()+strTrue[1:].lower(),val)
	
