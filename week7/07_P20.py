data=sorted([i.replace("\n","").split(";")[::-1] for i in open("hotels.txt")])[::-1]
star=int(input().strip())
st=True
for i in data:
    if int(i[1]) >= star:
        print(i[::-1][0],i[::-1][1],i[::-1][2])
        st=False
if st:
    print("Not Found")    