data=[line.strip().replace("\n","").split(":")[2:] for line in open("data.txt","r")]
sec=int(input())
Sum,n=0,0
for i in data:
	if sec == int(i[0]):
		Sum+=float(i[1])
		n+=1
if n==0:
	print("Not Found")
else:
	print(Sum/n)