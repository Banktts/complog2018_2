x=input().replace(" ","").lower()
print("yes" if x == x[::-1] else "no")