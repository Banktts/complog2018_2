x=int(input())
st=False
for i in range((x//2),1,-1):
    if x%i == 0 :
        print(i,end=" ")
        st=True
if st==False:
    print("Prime Number")