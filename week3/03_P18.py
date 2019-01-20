x=int(input())
for i in range(2,(x//2)+1):
    st=False
    for j in range(2,(i//2)+1):
        if i%j == 0  and i!=j :
            st=True
    if st==False and x%i==0:
        print(i,end=" ")
st=False
for i in range(2,(x//2)+1):
    if x%i == 0  and x!=i :
        st=True
if st==False and x>1:
    print(x,end=" ")