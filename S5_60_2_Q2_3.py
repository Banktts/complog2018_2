SubjectInDepartment={}
Subject=set()
Department=set()
Student=set()
StudentRegis=set()
StudentInDepartment={}
score=[]
for i in range(int(input().strip())):
  x=input().strip().split(",")
  if len(x)==2 and x[0] not in Subject:
    Subject.add(x[0])
    SubjectInDepartment[x[0]]=x[1]
    if x[1] not in Department:
      Department.add(x[1])
      StudentInDepartment[x[1]]=set()
for i in range(int(input().strip())):
  x=input().strip()
  if x not in StudentRegis:
    StudentRegis.add(x)
    x=x.split(",")
    if len(x)==2 and x[0] in Subject:
      StudentInDepartment[SubjectInDepartment[x[0]]].add(x[1])
      if x[1] not in Student:
        Student.add(x[1])
        score.append(0)
Search=input().strip().split(":")
Student=sorted(list(Student))
for x in Search:
  if x in Department :
    for y in Student:
      if y in StudentInDepartment[x]:
        score[Student.index(y)]+=1
for i in range(len(Search),0,-1):
  m=score.count(i)
  if m!=0:
    print("registered in",i,"faculty:",m,"student")
    for j in range(len(score)):
      if i==score[j]:
        print(Student[j])
  else:
    print("registered in",i,"faculty:",0,"student")