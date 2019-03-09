x=input().strip().split()
n=int(input())
cou=0
dataDic={}
for i in x:
  dataDic[str(int(i))]= True
for i in x:
  try:
    dataDic[str(n-int(i))]
    cou+=1
  except:
    pass
print(cou//2)