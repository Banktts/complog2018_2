n=int(input())
dicDepartment={}
dicStudent={}
dicStudentCompleted={}
for i in range(n):
    x=input().strip().split()
    dicDepartment[x[0]]=int(x[1])
n=int(input())
for i in range(n):
    x=input().strip().split()
    dicStudent[float(x[1])]=[x[0]]+x[2:]
for i in sorted(dicStudent.keys())[::-1]:
    for j in range(1,5):
        Department=dicStudent[i][j]
        if dicDepartment[Department]>0:
            dicStudentCompleted[int(dicStudent[i][0])]=Department
            dicDepartment[Department]-=1
            break
[print(i,dicStudentCompleted[i]) for i in sorted(dicStudentCompleted)]


