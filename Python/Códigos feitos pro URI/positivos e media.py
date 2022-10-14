contador = 0

#somador = soma
somador = 0
for index in range(6):
    valor = float(input())
    if valor > 0:
        contador += 1
        somador += valor

print('%d valores positivos' %contador)
print('%.1f' %(somador/contador))
