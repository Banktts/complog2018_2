x=input().strip().replace("<","").replace(">","").split(",")
y=input().strip().replace("<","").replace(">","").split(",")
total=0
for i in range(len(x)):
    total+=int(x[i])*int(y[i])
print(total)