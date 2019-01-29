x=input()
y=input()
xN=x.lower().replace(" ","")
yN=y.lower().replace(" ","")
if len(xN) != len(yN):
    print(x,y)
else:
    for i in xN:
        if i in yN:
            xN=xN[:xN.index(i)]+xN[xN.index(i)+1:]
            yN=yN[:yN.index(i)]+yN[yN.index(i)+1:]
    if xN == yN:
        print(x)
    else:
        print(x,y)