dt1=input().split(" ")
dt2=input().split(" ")
max1,volume1=int(dt1[0]),int(dt1[1])
max2,volume2=int(dt2[0]),int(dt2[1])
volume_all=volume1+volume2
if volume_all<=max2:
    print(0,volume_all)
else:
    print(volume_all-max2,max2)