choices={}
max_admitted={}
sorted_applicants={}
unassigned=[]
admitted={}
for i in range(int(input().strip())):
    tmp=input().strip().split()
    choices[tmp[0]]=tmp[1:]
    unassigned.append(tmp[0])
for i in range(int(input().strip())):
    tmp=input().strip().split()
    max_admitted[tmp[0]]=int(tmp[1])
    sorted_applicants[tmp[0]]=tmp[2:]
    admitted[tmp[0]]=[]
while len(unassigned) !=0:
    sid=unassigned.pop()
    if len(choices[sid]) !=0:
        pid=choices[sid].pop(0)
        admitted[pid].append(sid)
        if max_admitted[pid] < len(admitted[pid]):
            tmp=[]
            n=0
            for j in sorted_applicants[pid]:
              if n==max_admitted[pid]:
                break
              elif j in admitted[pid]:
                tmp.append(j)
                n+=1
            S=list(set(admitted[pid])-set(tmp))[0]
            unassigned.append(S)
            admitted[pid]=tmp
for i in sorted(admitted.keys()):
    print(i,end=" ")
    for j in sorted(admitted[i]):
        print(j,end=" ")
    print()
        
