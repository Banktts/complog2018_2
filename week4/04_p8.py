STR=input()
slice_part=input().split(" ")
print(STR[:int(slice_part[0])]+STR[int(slice_part[1]):int(slice_part[0])-1:-1]+STR[int(slice_part[1])+1:])
