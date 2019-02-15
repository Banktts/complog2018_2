m=int(input())
first_score=0
sec_score=0
for i in range(m):
    if m-i !=1:
        for j in range(3):
            x=input().strip()
            tmp=x.split(" ")
            first,second=tmp[0],tmp[1]
            if first != second:
                if "R" in x and "S" in x:
                    if first == "R":
                        first_score+=1
                    else:
                        sec_score+=1
                elif "S"in x and "P" in x:
                    if first == "S":
                        first_score+=1
                    else:
                        sec_score+=1
                elif "P"in x and "R"in x:
                    if first == "P":
                        first_score+=1
                    else:
                        sec_score+=1
    else:
        x=input().strip()
        tmp=x.split(" ")
        first,second=tmp[0],tmp[1]
        last_first=0
        last_second=0
        if first != second:
            if "R" in x and "S" in x:
                if first == "R":
                    last_first+=1
                    first_score+=1
                else:
                    last_second+=1
                    sec_score+=1
            elif "S"in x and "P" in x:
                if first == "S":
                    last_first+=1
                    first_score+=1
                else:
                    last_second+=1
                    sec_score+=1
            elif "P"in x and "R"in x:
                if first == "P":
                    last_first+=1
                    first_score+=1
                else:
                    last_second+=1
                    sec_score+=1
        else:
            for j in range(2):
                x=input().strip()
                tmp=x.split(" ")
                first,second=tmp[0],tmp[1]
                if first != second:
                    if "R" in x and "S" in x:
                        if first == "R":
                            first_score+=1
                        else:
                            sec_score+=1
                    elif "S"in x and "P" in x:
                        if first == "S":
                            first_score+=1
                        else:
                            sec_score+=1
                    elif "P"in x and "R"in x:
                        if first == "P":
                            first_score+=1
                        else:
                            sec_score+=1
print(first_score,sec_score)
if last_first<last_second:
    print("Player 2 wins")
elif last_second<last_first:
    print("Player 1 wins")
else:
    print("Tie")

