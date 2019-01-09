x=input()
SUM=0
for i in range(10,1,-1):
	SUM+=i*int(x[10-i])
pr=11-SUM%11
if pr == 11:
	c=0
else:
	c=pr
print(x+str(c))