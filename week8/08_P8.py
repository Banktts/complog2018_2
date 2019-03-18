subject,data=set(),{}
while True:
    x=input().strip()
    if x == "-1":
        break
    x=x.split()
    for i in range(1,len(x)):
        if x[i] in subject:
            data[x[i]].append(x[0])
        else:
            data[x[i]]=[x[0]]
            subject.add(x[i])
x,y=[i for i in input().strip().split()]
if x in subject and y in subject:
    print(len(set(data[x]).intersection(set(data[y]))),end=" ")
    print(len(set(data[x])^set(data[y])),end=" ")
    print(len(set(data[x]).union(set(data[y]))))
elif x in subject:
    print(0,end=" ")
    print(len(data[x]),end=" ")
    print(len(data[x]),end=" ")
elif y in subject:
    print(0,end=" ")
    print(len(data[y]),end=" ")
    print(len(data[y]),end=" ")
else:
    print(0,end=" ")
    print(0,end=" ")
    print(0,end=" ")