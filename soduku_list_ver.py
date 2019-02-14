data=[]
row="Row: "
col="Col: "
box="Box: "
#file=open("file1.txt","r")
data=[]
#for i in file:
	#data.append(i.strip().replace("\n",""))
for i in range(9):
	data.append(input().strip())
com=input()
for i in range(9):
	if "123456789" != "".join(sorted(data[i])):
		row+=str(i+1)+" "
for i in range(9):
	tmp=data[0][i]+data[1][i]+data[2][i]+data[3][i]+data[4][i]+data[5][i]+data[6][i]+data[7][i]+data[8][i]
	if "123456789" != "".join(sorted(tmp)):
		col+=str(i+1)+" "
for i in range(9):
	if 0<=i<=2:
		tmp=data[0][3*i]+data[0][3*i+1]+data[0][3*i+2]+data[1][3*i]+data[1][3*i+1]+data[1][3*i+2]+data[2][3*i]+data[2][3*i+1]+data[2][3*i+2]
	elif 3<=i<=5:
		i=i-3
		tmp=data[3][3*i]+data[3][3*i+1]+data[3][3*i+2]+data[4][3*i]+data[4][3*i+1]+data[4][3*i+2]+data[5][3*i]+data[5][3*i+1]+data[5][3*i+2]
		i=i+3
	else:
		i=i-6
		tmp=data[6][3*i]+data[6][3*i+1]+data[6][3*i+2]+data[7][3*i]+data[7][3*i+1]+data[7][3*i+2]+data[8][3*i]+data[8][3*i+1]+data[8][3*i+2]
		i=i+6 
	if "123456789" != "".join(sorted(tmp)):
		box+=str(i+1)+" "
if row=="Row: ":
	row+="OK"
if col=="Col: ":
	col+="OK"
if box=="Box: ":
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
	
