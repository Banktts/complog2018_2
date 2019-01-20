lst=input().split(" ")
n,ch=int(lst[0]),int(lst[1])
if ch==3:
    for i in range(1,n+1):
        print("("+str(i)+","+str(n-i+1)+")")
elif ch==2:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("("+str(i)+","+str(j)+")")
elif ch==1:
    for i in range(1,n+1):
        for j in range(i,n+1):
            print("("+str(i)+","+str(j)+")")