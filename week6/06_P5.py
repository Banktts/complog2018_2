st=True
lst=[]
final=0
while st:
    x=int(input())
    if x<0:
        final=x
        st=False
    else:
        lst.append(x)
for i in lst:
    print(i+final)