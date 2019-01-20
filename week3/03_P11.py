n=int(input())
SUM=0
if n==0:
    print("No Data")
else:
    for i in range(n):
        SUM+=float(input())
    print(SUM/n)
