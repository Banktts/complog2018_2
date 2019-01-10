dt1=[int(i) for i in input().strip().split(" ")]
dt2=[int(i) for i in input().strip().split(" ")]
x1,y1,c1=dt1[0],dt1[1],dt1[2]
x2,y2,c2=dt2[0],dt2[1],dt2[2]
maxdt1abs,maxdt2abs=max(list(map(lambda x: abs(x),dt1[:2]))),max(list(map(lambda x: abs(x),dt2[:2])))
rt= maxdt2abs/maxdt1abs if maxdt1abs<=maxdt2abs else maxdt1abs/maxdt2abs
if maxdt1abs >= maxdt2abs:
    x2,y2,c2=dt2[0]*rt,dt2[1]*rt,dt2[2]*rt
else:
    x1,y1,c1=dt1[0]*rt,dt1[1]*rt,dt1[2]*rt
if abs(x1)==abs(x2) and abs(y1)==abs(y2):
    if c1==c2 or (x1==x2*(-1)*rt and y1==y2*(-1)*rt and c1==c2*(-1)*rt  ):
        print("many solutions")
    else:
        print("no solution")
else:
    print("one solution")