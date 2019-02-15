sc_stroke=0
sc_sum=0
for i in range(9):
    x=input().strip().split(" ")
    par=int(x[0])
    stroke=int(x[1])
    sc_stroke+=stroke
    sum_sc=stroke-par
    if sum_sc<=0:
        sc_sum+=2
    elif sum_sc==1:
        sc_sum+=1
print(sc_stroke)
con_sc=18-sc_sum
print(con_sc)
f_sc=sc_stroke-con_sc
print(f_sc)