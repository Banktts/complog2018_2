x=input().strip().split()
n=int(input())
cn=0
for i in range(len(x)):
    for j in x[:i]+x[i+1:]:
        if int(x[i])+int(j)==n:
            cn+=1
print(cn//2)