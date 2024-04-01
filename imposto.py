salario = float(input("Digite seu salário mensal: "))

if salario <= 2000:
    imposto = 0
elif salario <= 3500:
    imposto = salario * 0.1
else:
    imposto = salario * 0.15

print(f"O valor do imposto a pagar é: R$ {imposto:.2f}")