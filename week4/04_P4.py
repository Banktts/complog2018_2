STR=input()
slice_part=input().split(" ")
print(STR[0:int(slice_part[0])]+STR[int(slice_part[0]):int(slice_part[1])+1][::-1]+STR[int(slice_part[1])+1:len(STR)])
