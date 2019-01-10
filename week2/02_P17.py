base_10=int(input())
if base_10>=0 and base_10<81:
    bs=[]
    for i in range(4):
        bs.append(str(base_10%3))
        base_10=base_10//3
    bs=bs[::-1]
    print("".join(bs))
else:
    print("Error : Out of range")
