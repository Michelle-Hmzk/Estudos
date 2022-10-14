num = input().split(" ")

a,b = tuple(num)
a = int(a) #é o codigo
b = int(b) #é a quantidade

if a == 1:
    print("Total: R$ %.2f" %(b*4.00))
if a == 2:
     print("Total: R$ %.2f" %(b*4.50))
if a == 3:
     print("Total: R$ %.2f" %(b*5.00))
if a == 4:
     print("Total: R$ %.2f" %(b*2.00))
if a == 5:
     print("Total: R$ %.2f" %(b*1.50))
