x=input().lower().replace("\'"," ").replace("\""," ").replace("."," ").replace(","," ").split(" ")
y=input().lower()
print("Found" if y in x else "Not Found")