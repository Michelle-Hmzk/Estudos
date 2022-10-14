peca = input().split(" ")
peca2 = input().split(" ")

a,b,c = peca
a = int(a)
b = int(b)
c = float(c)

d,e,f = peca2
d = int(d)
e = int(e)
f = float(f)

p = (b*c)+(e*f)

print("VALOR A PAGAR: R$ %.2f" %p )