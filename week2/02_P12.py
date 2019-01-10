dt=sorted([int(i) for i in input().split(" ")])
s1,s2,s3=dt[0],dt[1],dt[2]
print("YES" if s1+s2>s3 else "NO")