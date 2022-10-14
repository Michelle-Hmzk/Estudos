#for = função que repete algo quantas vezes foi pedido
contador = 0

for index in range(6):
    #variavel local = só existe dentro da função, fora não se acessa. 
    valor = float(input())
    if valor > 0:
        #contador = start com variavel e guarda
        contador += 1

print('%d valores positivos' %contador)

    