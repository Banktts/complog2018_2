grade=[]
status=True
while status == True:
    x=int(input())
    if x == -1:
        status = False
    else:
        grade.append(x)
for i in range (len(grade)):
    if grade[i]>=80 and grade[i]<=100:
        print("A")
    elif grade[i]>=75 and grade[i]<=79:
        print("B+")
    elif grade[i]>=70 and grade[i]<=74:
        print("B")
    elif grade[i]>=65 and grade[i]<=69:
        print("C+")
    elif grade[i]>=60 and grade[i]<=64:
        print("C")
    elif grade[i]>=55 and grade[i]<=59:
        print("D+")
    elif grade[i]>=50 and grade[i]<=54:
        print("D")
    elif grade[i]>=0 and grade[i]<=50:
        print("F")
    else:
        print("Error")