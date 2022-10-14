sal = float(input())

if (sal >= 0 and sal<= 400.00):
    print("Novo salario: %.2f" %(sal+(sal*15/100)))
    print("Reajuste ganho: %.2f" %(sal*15/100))
    print("Em percentual: 15 %")

if (sal>= 400.01 and sal <= 800.00):
    print(":Novo salario: %.2f" %(sal+(sal*12/100)))
    print("Reajuste ganho: %.2f" %(sal*12/100))
    print("Em percentual: 12 %")
 
if (sal>= 800.01 and sal <= 1200.00):
    print("Novo salario: %.2f" %(sal+(sal*10/100)))
    print("Reajuste ganho: %.2f" %(sal*10/100))
    print("Em percentual: 10 %") 

if (sal>= 1200.01 and sal <= 2000.00):
    print("Novo salario: %.2f" %(sal+(sal*7/100)))
    print("Reajuste ganho: %.2f" %(sal*7/100))
    print("Em percentual: 7 %" )

if (sal>= 2000.01):
    print("Novo salario: %.2f" %(sal+(sal*4/100)))
    print("Reajuste ganho: %.2f" %(sal*4/100))
    print("Em percentual: 4 %")
