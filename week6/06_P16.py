x=[int(x) for x in input().split(", ")]
n=0
for i in range(1,len(x)):
    if x[i]<0 and x[i-1]>=0:
        n+=1
print(n)