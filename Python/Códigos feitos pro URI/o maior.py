num = input().split(" ")

A,B,C = num
A = int(A)
B = int(B)
C = int(C)

maior = (A + B + abs(A-B))/2
mai = (maior + C + abs(maior-C))/2

print("%i eh o maior" %mai)

