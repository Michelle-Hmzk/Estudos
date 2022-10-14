A,B = map(int,input().split(" "))

if (A == B):
    print("O JOGO DUROU 24 HORA(S)")

elif (B - A > 0):
    print("O JOGO DUROU %i HORA(S)" %(B - A))

elif (B - A < 0):
    print("O JOGO DUROU %i HORA(S)" %(24+(B - A)))