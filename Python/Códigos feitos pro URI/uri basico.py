# #area do circulo 

raio = float(input())

area = (3.14159 * (raio**2))

print("A=%.4f" %area)

#soma simples
A = int(input())
B = int(input())

SOMA = A + B

print("SOMA =",SOMA)

#produto simples
A = int(input())
B = int(input())

PROD = A*B

print("PROD =",PROD)

#salario com bonus
nom = input()

salfix = float(input())

totvendas = float(input())

tot = salfix + totvendas*15/100

print("TOTAL = R$ %.2f" %tot)

#esfera
R = int(input())

vol = (4/3) * 3.14159 * R**3

print("VOLUME = %.3f" %vol)

#distancia entre dois pontos
num = input().split(" ")
x1,y1 = tuple(num)
x1 = float(x1)
y1 = float(y1)

num = input().split(" ")
x2 , y2 = tuple(num)
x2 = float(x2)
y2 = float(y2)

dist =((x2-x1)**2+(y2-y1)**2)**0.5

print("%.4f" %dist)

#distancia
km = int(input())

X = 60
Y = 90

minutos = km * 2

print("%d minutos" %minutos)

#media 2
A = float(input())
B = float(input())
C = float(input())

med = ((A*2) + (B*3) + (C*5))/10

print("MEDIA = %.1f" %med)

#gasto de combustivel
hr = int(input())
vel = int(input())

comb = vel/12 * hr

print("%.3f" %comb)

#cedulas
val = int(input())

print(val)

x = val//100
print("%d nota(s) de R$ 100,00" %x)

y= val%100//50
print("%d nota(s) de R$ 50,00" %y)

h = val%100%50/20
print("%d nota(s) de R$ 20,00" %h)

i = val%100%50%20/10
print("%d nota(s) de R$ 10,00" %i)

j= val%100%50%20%10/5
print("%d nota(s) de R$ 5,00" %j)

k = val%100%50%20%10%5/2
print("%d nota(s) de R$ 2,00" %k)

l = val%100%50%20%10%5%2/1
print("%d nota(s) de R$ 1,00" %l)

#conversao de tempo
tempo = int(input())

a = tempo//3600 
b = tempo%3600/60
c  = tempo%3600%60

print('%i:%i:%i' %(a,b,c) )

#idade em dias
dias = int(input())

A = dias/365
print("%d ano(s)" %A)

M = dias%365/30
print("%d mes(es)" %M)

D = dias%365%30
print("%d dia(s)" %D)

#notas e moedas
val = float(input())

print("NOTAS:")

x = val//100
print("%d nota(s) de R$ 100.00" %x)

y= val%100//50
print("%d nota(s) de R$ 50.00" %y)

h = val%100%50/20
print("%d nota(s) de R$ 20.00" %h)

i = val%100%50%20/10
print("%d nota(s) de R$ 10.00" %i)

j= val%100%50%20%10/5
print("%d nota(s) de R$ 5.00" %j)

k = val%100%50%20%10%5/2
print("%d nota(s) de R$ 2.00" %k)

print("MOEDAS:")

l = val%100%50%20%10%5%2/1
print("%d moeda(s) de R$ 1.00" %l)

m = val%100%50%20%10%5%2%1/0.5
print("%d moeda(s) de R$ 0.50" %m)

n = val%100%50%20%10%5%2%1%0.5/0.25
print("%d moeda(s) de R$ 0.25" %n)

o = val%100%50%20%10%5%2%1%0.5%0.25/0.10
print("%d moeda(s) de R$ 0.10" %o)

p = val%100%50%20%10%5%2%1%0.5%0.25%0.10/0.05
print("%d moeda(s) de R$ 0.05" %p)

q = val%100%50%20%10%5%2%1%0.5%0.25%0.10%0.05/0.009
print("%d moeda(s) de R$ 0.01" %q)

#Fórmula de Bhaskara
val = input().split(" ")
a,b,c = val
a = float(a)
b = float(b)
c = float(c)


if (a == 0) or (b ** 2 - 4 * a * c) < 0:
    print("Impossivel calcular")

else:
    R1 = (-(b) + ((b**2)-(4*a*c))**(0.5))/(2*a) 
    R2 = (-(b) - ((b**2)-(4*a*c))**(0.5))/(2*a)
    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)

#intervalo

inter = float(input())

if (inter < 0) or (inter > 100):
    print("Fora de intervalo.")

elif (inter >= 0) and (inter <= 25 ):
    print("Intervalo [0,25]")

elif (inter > 25) and (inter <= 50 ):
    print("Intervalo (25,50]")

elif (inter > 50) and (inter <= 75 ):
    print("Intervalo (50,75]")

elif (inter > 75) and (inter <= 100 ):
    print("Intervalo (75,100]")