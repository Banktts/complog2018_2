n=int(input())
lst=[]
for i in range(1,n//2):
    for j in range(1,n//2):
        if i**2+j**2==(n-i-j)**2:
            if n-i-j not in lst:
                lst.append(n-i-j)
if len(lst) == 1:
    print(lst[0])
else:
    print(max(lst))