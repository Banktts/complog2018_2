x=input()
xl=""
for i in range(len(x)):
	if x[i] not in x[i+1:] and x[i] not in xl:
		xl=xl+x[i]
	elif x[i] in x[:i] and x[i] not in xl:
		xl=xl+x[i]
print(xl)
