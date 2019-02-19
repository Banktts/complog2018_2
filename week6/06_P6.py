n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
x=input().split()
print(sum(lst[int(x[0]):int(x[1])+1]))