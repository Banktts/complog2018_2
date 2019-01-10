x=int(input())-543
print("29" if (x%4==0 and x%100!=0) or x%400==0 else "28")