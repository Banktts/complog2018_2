SUM=0
status=True
while status == True:
    x=int(input())
    if x == -1:
        status = False
    else:
        if x%2==0:
            SUM+=x
print(SUM)