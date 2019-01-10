DayOfMonth=[31,[28,29],31,30,31,30,31,31,30,31,30,31]
dt=input().split(" ")
m=int(dt[0])
y=int(dt[1])-543
if m!=2:
    print(DayOfMonth[m-1])
else:
    print(DayOfMonth[1][1] if (y%4==0 and y%100!=0) or y%400==0 else DayOfMonth[1][0])
