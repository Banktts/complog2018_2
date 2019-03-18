unassigned=[]
admitted={}
choices={}
recieve={}
for i in range(int(input().strip())):
    tmp=input().strip().split()
    choices[tmp[0]]=tmp[1:]
    unassigned.append(tmp[0])
for i in range(int(input().strip())):
    tmp=input().strip().split()
    recieve[tmp[0]]=[int(tmp[1])]+tmp[2:]
    admitted[tmp[0]]=[]
while len(unassigned) >0:
    select=unassigned.pop()
    ChoiceHasSelect=choices[select].pop(0)
    if recieve[ChoiceHasSelect][0] > 0:
        admitted[ChoiceHasSelect].append(select)
        recieve[ChoiceHasSelect][0]-=1
    else:
        Compare=admitted[ChoiceHasSelect]
        Case=recieve[ChoiceHasSelect][1:]
        st=True
        for i in Compare:
            if Case.index(i)>Case.index(select):
                x=admitted[ChoiceHasSelect].pop(admitted[ChoiceHasSelect].index(i))
                admitted[ChoiceHasSelect].append(select)
                if len(choices[x]) !=0:
                    unassigned.append(x)
                st=False
                break
        if st and len(choices[select])!=0:
            unassigned.append(select)
try:
    admittedKey=sorted([int(i) for i in admitted.keys()])
except:
    admittedKey=sorted(admitted.keys())
for i in admittedKey:
    print(i,end=" ")
    try:
        tmp=sorted([int(i) for i in admitted[str(i)]])
    except:
        tmp=sorted(admitted[str(i)])
    for j in tmp:
        print(j,end=" ")
    print()



