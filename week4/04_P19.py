x=input()
upArg=input()
downArg=input()
xl=""
for i in range(len(x)):
	if x[i] in upArg:
		xl=xl+downArg[upArg.index(x[i])]
	elif x[i] in downArg:
		xl=xl+upArg[downArg.index(x[i])]
	else:
		xl=xl+x[i]
print(xl)
