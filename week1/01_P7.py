'''
def Pro(SUM,n):
	if n<5:
		x=float(input())
		return Pro(SUM+x,n+1)
	else:
		return SUM/5
print(Pro(0,0))

'''
#simple code see below
x1=float(input())
x2=float(input())
x3=float(input())
x4=float(input())
x5=float(input())
sum_data=x1+x2+x3+x4+x5
avg=sum_data/5
print(avg)