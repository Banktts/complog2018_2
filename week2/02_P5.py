max=min=float(input())
for i in range(5):
    i=float(input())
    if i>max:
        max=i
    if i < min:
        min=i
print(min,max)