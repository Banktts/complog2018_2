x=input()
xl=""
vowel=0
for i in range(len(x)):
	if ((ord(x[i]) >= 65 and ord(x[i]) <= 90) or (ord(x[i]) >= 97 and ord(x[i]) <= 122)):
		xl=xl+x[i]
xl=xl.lower()
for j in range(len(xl)):
	if "a" == xl[j] or "e" == xl[j] or "i" == xl[j] or "o" == xl[j] or "u" == xl[j] :
		vowel+=1
print(vowel,len(xl)-vowel)
	

