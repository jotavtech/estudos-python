idade = int(input("Digite sua idade: "))

if idade < 12 or idade > 60:
    valor = 15.00
else:
    valor = 25.00

print(f"O valor do ingresso é: R$ {valor:.2f}")