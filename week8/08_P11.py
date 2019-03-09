data={}
collected=[]
for i in open("books.txt"):
    tmp=i.strip().split(", ")
    data[tmp[0]]=tmp[1:]
search=input().strip().split(", ")
for i in data.keys():
    st=True
    for j in search:
        if j not in data[i]:
            st=False
    if st:
        collected.append(i)
[print(i) for i in sorted(collected)] if len(collected) != 0 else print("Not found")