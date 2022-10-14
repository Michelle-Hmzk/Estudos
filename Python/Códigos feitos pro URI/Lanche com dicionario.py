num = input().split(" ")

a,b = tuple(num)
a = int(a) #é o codigo
b = int(b) #é a quantidade

#key:value
dicionario = {
    1:4.00,
    2:4.50,
    3:5.00,
    4:2.00,
    5:1.50,
}
print("Total: R$ %.2f" %(b*dicionario.get(a)))
#no dicionairio eu posso usar o .get que fala o que quero pegar dele a partir da chave
