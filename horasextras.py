horas_extras = int(input("Digite o número de horas extras: "))
horas_faltadas = int(input("Digite o número de horas que o funcionário faltou: "))

limite_bonus = horas_faltadas * 1.5

if horas_extras > limite_bonus:
    print("Bônus de R$ 500.00")
else:
    print("Sem bônus")

    