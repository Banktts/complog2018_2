n = int(input()) 
st=False
rd=int(n**(1/2))+1
for x in range(rd):
    for y in range(rd):
        if x**2 + y**2 == n:
            if x<=y:
                print(x, y)
            st=True
if st==False:
    print("No solution")