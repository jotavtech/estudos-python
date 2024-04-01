nota1 = float(input("Digite a nota da 1a. avaliação: "))
nota2 = float(input("Digite a nota da 2a. avaliação: "))

media = (nota1 + nota2) / 2
print("A média do aluno é:", media)

if media >= 6:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado.")