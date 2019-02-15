com=open(input(),"r")
rec=open(input(),"r")
Comlst=[]
Reclst=[]
n=0
for i in com:
	Comlst.append(int(i))
	n+=int(i)
for i in rec:
	Reclst.append(float(i))
for i in Comlst:
	print(sum(Reclst[:i])/i)
	Reclst=Reclst[i:]