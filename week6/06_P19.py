data=[]
newdata_fruit=[]
newdata_name=[]
newdata_n=[]
newdata=[]
for i in open(input().strip(),"r"):
    data.append(i.replace("\n",""))
for i in data:
    tmp=i.split()
    fruit=tmp[0]
    name=tmp[1]
    if fruit not in newdata_fruit:
        newdata_fruit.append(fruit)
        newdata_name.append([])
    newdata_name[newdata_fruit.index(fruit)].append(name)
    
for i in range(len(newdata_fruit)):
    newdata_n.append(len(newdata_name[i]))
    tmp=[newdata_fruit[i]]
    tmp.append(newdata_name[i])
    newdata.append(tmp)
print(newdata)
print("The most favorite fruit is",newdata_fruit[newdata_n.index(max(newdata_n))])