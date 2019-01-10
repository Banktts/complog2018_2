DayOfMonth1=[31,28,31,30,31,30,31,31,30,31,30,31]
DayOfMonth2=[31,29,31,30,31,30,31,31,30,31,30,31]
d=int(input())
m=int(input())
y=int(input())-543
if m<2:
    print(m)
else:
    if (y%4==0 and y%100!=0) or y%400==0: ##29day
        for i in range(m-1):
            d+=DayOfMonth2[i]
        print(d)
    else: #28day
        for i in range(m-1):
            d+=DayOfMonth1[i]
        print(d)
