x=input().lower()
n=0
for j in range(97,123):
    if j!=97 and j!=101 and j!=105 and j!=111 and j!=117:
        x=x.replace(chr(j),",")
m=x.split(",")
n=len(m)
de=0
for j in m:
    if j =="":
        de+=1
print(n-de)