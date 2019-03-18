name,subject,data=set(),set(),{}
for i in range(int(input())):
    x=[i.strip() for i in input().strip().split(",")]
    name.add(x[0])
    for i in range(1,5):
        if x[i] in subject:
            data[x[i]].append(x[0])
        else:
            subject.add(x[i])
            data[x[i]]=[x[0]]
search=[i.strip() for i in input().strip().split(",")]
for i in search:
    if i in subject:
        print(i,"->",end="")
        [print(" "+data[i][j]+",",end="") if j+1!=len(data[i]) else print(" "+data[i][j]) for j in range(len(data[i]))]
    else:
        print(i,"->","Not found")