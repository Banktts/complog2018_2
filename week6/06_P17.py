x=[int(x) for x in input().split()]
n=len(x)
player1=0
player2=0
for i in range(n):
    if x[0]>x[-1]:
        sc=x[0]
    else:
        sc=x[-1]    
    if (i+1)%2==0:
        player2+=sc
    else:
        player1+=sc
    x.remove(sc)
print(player1)
print(player2)
print(1 if player1>player2 else 2 if player2>player1 else 0)