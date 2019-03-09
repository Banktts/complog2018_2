data,completedSearch={},[]
for i in range(int(input())):
    x=input().strip().split()
    data[x[0]]=x[1:]
search=input().strip().split()
for i in data.keys():
    st=True
    for j in range(len(search)):
        if search[j] not in data[i]:
            st=False
    if st:
        completedSearch.append(i)
[print(i,data[i][0],data[i][1],data[i][2]) for i in sorted(completedSearch)] if len(completedSearch)!=0 else print("Not Found")
    
