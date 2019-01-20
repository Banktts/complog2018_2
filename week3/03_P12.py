SUM=0
n=0
status=True
while status == True:
    x=float(input())
    if x == -1:
        status = False
    else:
        SUM+=x
        n+=1
if n==0:
    print("No Data")
else:
    print(SUM/n)