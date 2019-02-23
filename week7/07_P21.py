data=sorted([i.split()[::-1] for i in open("circulations.txt")])
st=True
x=input().strip()
for i in data:
  if int(i[0])<=int(x):
    print(i[::-1][0],i[::-1][1],i[::-1][2])
    st=False
if st:
  print("Not Found")