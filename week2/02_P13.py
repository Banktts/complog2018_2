startHr=int(input())
startMin=int(input())
stopHr=int(input())
stopMin=int(input())
parkmin=stopHr*60+stopMin-(startHr*60+startMin)
price=0
if stopHr < startHr or(stopHr == startHr and stopMin<startMin):
    price=200
elif parkmin<=15:
    price=0
elif parkmin>15 and parkmin<=180:
    if parkmin%60==0:
        price+=(parkmin//60)*10
    else:
        price+=(parkmin//60)*10+(1*10)
elif parkmin>180 and parkmin<=360:
    price+=30
    if parkmin%60==0:
        price+=((parkmin-180)//60)*20
    else:
        price+=((parkmin-180)//60)*20+(1*20)
else:
    price+=200
print(price)
