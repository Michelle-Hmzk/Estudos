num = input().split(" ")

A, B = num
A = int(A)
B = int(B)

if B>A:
    if B%A == 0:
        print('Sao Multiplos')
    else: 
        print('Nao sao Multiplos')
    
if A > B:
    if A%B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if A == B:
    print('Sao Multiplos')