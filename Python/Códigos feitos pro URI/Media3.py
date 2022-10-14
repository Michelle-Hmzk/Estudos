A, B, C, D  = map(float,input().split(" "))

med = ((A*2)+(B*3)+(C*4)+D)/10

print("Media: %.1f" %med)

if (med < 5):
    print("Aluno reprovado.")

if (med >= 5) and (med <=6.9):
    print("Aluno em exame.")
    nota = float(input())
    print("Nota do exame: %.1f" %nota)
    if (med + nota)/2 >= 5:
        print("Aluno aprovado.")
        print("Media final: %.1f" %((med + nota)/2))
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" %((med + nota)/2))

if (med >= 7):
    print("Aluno aprovado.")




