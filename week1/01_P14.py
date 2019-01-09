x=input()
SUM=0
for i in range(13,1,-1):
	SUM+=i*int(x[13-i])
n13=(11-SUM%11)%10
print(n13)