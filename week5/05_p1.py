data=[line.strip().split(" ") for line in open("score.txt","r")]
check=input()
st=False
for i in data:
	if i[0]==check:
		print(i[1])
		st=True
if st == False:
	print("Not Found")