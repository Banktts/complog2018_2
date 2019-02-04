n=int(input())
x=""
st=True
for i in range(n-1):
	tmp=input()+' '
	x=x+tmp
x=x+input()
tmp=""
for j in range(len(x)):
	tmp=tmp+x[j]
	for i in x.split(' '):
		if tmp not in i:
			st=False
	if st==False:
		tmp=tmp[:j]
		break
if len(tmp)!=1 and len(tmp)!=0:
	print(tmp)
else:
	print("NO COMMON PREFIX")
x=x[::-1]
st=True
tmp=""
for j in range(len(x)):
	tmp=tmp+x[j]
	for i in x.split(' '):
		if tmp not in i:
			st=False
	if st==False:
		tmp=tmp[:j]
		break
if len(tmp)!=1 and len(tmp)!=0:
	print(tmp[::-1])
else:
	print("NO COMMON SUFFIX")
