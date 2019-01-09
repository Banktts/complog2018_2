hr1=int(input())
min1=int(input())
sec1=int(input())
hr2=int(input())
min2=int(input())
sec2=int(input())
t1=hr1*60*60+min1*60+sec1
t2=hr2*60*60+min2*60+sec2
S=t2-t1
hr=S//3600
min=(S-hr*3600)//60
sec=S-(min*60)-hr*3600
if hr<0:
	hr=24+hr
print(str(hr)+":"+str(min)+":"+str(sec))