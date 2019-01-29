x=input().lower()
MAX=0
n=MAX
tmp=""
for i in x:
	if tmp != i:
		tmp=i
		if n>MAX:
			MAX=n	
		n=1
	else:
		n+=1
if n>MAX:
	MAX=n
print(MAX)
