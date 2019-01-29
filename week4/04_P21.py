n=int(input())
lst=[]
lstlen=[]
for i in range(n):
    x=input().strip()
    lst.append(x)
    lstlen.append(len(x))
Min=min(lstlen)
for i in range(Min+1,-1,-1):
    tmp=lst[0][:i]
    st1=True
    for j in lst:
        if j[:i] != tmp:
            st1=False
            break
    if st1==True:
        break
if st1 == False or tmp=="":
    print("NO COMMON PREFIX")
else:
    print(tmp)
for i in range(Min+1,-1,-1):
    tmp=lst[0][::-1][:i]
    st2=True
    for j in lst:
        if j[::-1][:i] != tmp:
            st2=False
            break
    if st2==True:
        break
if st2 == False or tmp =="":
    print("NO COMMON SUFFIX")
else:
    print(tmp[::-1])