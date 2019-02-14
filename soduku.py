x=""
row="Row: "
col="Col: "
box="Box: "
######## check test case from file1
#file=open("file1.txt","r")
#data=[]
#for i in file:
#	data.append(i.strip().replace("\n",""))
#x="".join(data)
for i in range(9):
	x+=input().strip()
com=input().strip()
#row
for i in range(9):
	tmp=""
	for j in range(9):
		tmp+=x[(i*9)+j]
	if not(("9" in tmp) and ("8" in tmp)and ("7" in tmp) and ("6" in tmp) and ("5" in tmp)and ("4" in tmp) and ("3" in tmp) and ("2" in tmp) and ("1" in tmp)):
		row+=str(i+1)+" "
#col
for i in range(9):
	tmp=""
	for j in range(9):
		tmp+=x[i+(j*9)]
	if not(("9" in tmp) and ("8" in tmp)and ("7" in tmp) and ("6" in tmp) and ("5" in tmp)and ("4" in tmp) and ("3" in tmp) and ("2" in tmp) and ("1" in tmp)):
		col+=str(i+1)+" "
#box
for i in range(9):
	if i<3:
		tmp=x[(i*3):(i*3)+3]+x[(i*3)+9:(i*3)+12]+x[(i*3)+18:(i*3)+21]
	elif i<6:
		i=i-3
		tmp=x[(i*3)+27:(i*3)+3+27]+x[(i*3)+9+27:(i*3)+12+27]+x[(i*3)+18+27:(i*3)+21+27]
		i=i+3
	else:
		i=i-6
		tmp=x[(i*3)+27+27:(i*3)+3+27+27]+x[(i*3)+9+27+27:(i*3)+12+27+27]+x[(i*3)+18+27+27:(i*3)+21+27+27]
		i=i+6
	if not(("9" in tmp) and ("8" in tmp)and ("7" in tmp) and ("6" in tmp) and ("5" in tmp)and ("4" in tmp) and ("3" in tmp) and ("2" in tmp) and ("1" in tmp)):
		box+=str(i+1)+" "
if len(row) == 5:
	row+="OK"
if len(col) == 5:
	col+="OK"
if len(box) == 5:
	box+="OK"
if com == "R":
	print(row)
elif com=="C":
	print(col)
elif com=="B":
	print(box)
else:
	print(row)
	print(col)
	print(box)
		
		

	
		
