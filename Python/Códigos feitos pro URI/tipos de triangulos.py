trig = input().split(" ")
trig.sort()

A, B, C = trig
A = float(A)
B = float(B)
C = float(C)

if A >= (B+C):
    print('NAO FORMA TRIANGULO')

else:
    if A**2 == ((B**2)+(C**2)):
        print('TRIANGULO RETANGULO')

    if A**2 > ((B**2)+(C**2)):
        print('TRIANGULO OBTUSANGULO')

    if A**2 < ((B**2)+(C**2)):
        print('TRIANGULO ACUTANGULO')

    if (A == B == C):
        print('TRIANGULO EQUILATERO')
 
    if (A == B and A != C) or (B == C and B != A) or (A ==C and A!=B):
        print('TRIANGULO ISOSCELES')