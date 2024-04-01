nota1 = float(input("Digite a nota da 1a. avaliação: "))
nota2 = float(input("Digite a nota da 2a. avaliação: "))

media = (nota1 + nota2) / 2
print("A média do aluno é:", media)

if media >= 6:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado.")



    numero = float(input("Digite um número: "))

if numero > 50:
    print("O número é maior que 50.")
elif numero < 50:
    print("O número é menor que 50.")
else:
    print("O número é igual a 50.")

    valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("O maior valor é:", valor1)
else:
    print("O maior valor é:", valor2)


    valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 < valor2:
    print("Em ordem crescente:", valor1, valor2)
else:
    print("Em ordem crescente:", valor2, valor1)


    valor = float(input("Digite um valor: "))

if valor > 10:
    print("O valor digitado é maior que 10.")
else:
    print("O valor digitado é menor ou igual a 10.")


    numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o débito: "))
credito = float(input("Digite o crédito: "))

saldo_atual = saldo - debito + credito
print("Saldo atual:", saldo_atual)

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")


    quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2
print("Quantidade média:", quantidade_media)

if quantidade_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")


    valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
    desconto = valor_compra * 0.1
elif valor_compra >= 50:
    desconto = valor_compra * 0.05
else:
    desconto = 0

valor_total = valor_compra - desconto
print("Valor do desconto:", desconto)
print("Valor total a pagar:", valor_total)


horas_extras = int(input("Digite o número de horas extras: "))
horas_faltadas = int(input("Digite o número de horas que o funcionário faltou: "))

limite_bonus = horas_faltadas * 1.5

if horas_extras > limite_bonus:
    print("Bônus de R$ 500.00")
else:
    print("Sem bônus")


    lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")


    idade = int(input("Digite sua idade: "))

if idade < 12 or idade > 60:
    valor = 15.00
else:
    valor = 25.00

print(f"O valor do ingresso é: R$ {valor:.2f}")


temperatura = float(input("Digite a temperatura atual (em °C): "))

if temperatura < 15:
    print("Está frio.")
elif 15 <= temperatura <= 25:
    print("Está ameno.")
else:
    print("Está quente.")


    numero = int(input("Digite o número do seu candidato (1 para A, 2 para B, 3 para C, qualquer outro para nulo): "))

if numero == 1:
    print("Voto no candidato A.")
elif numero == 2:
    print("Voto no candidato B.")
elif numero == 3:
    print("Voto no candidato C.")
else:
    print("Voto nulo.")


    salario = float(input("Digite seu salário mensal: "))

if salario <= 2000:
    imposto = 0
elif salario <= 3500:
    imposto = salario * 0.1
else:
    imposto = salario * 0.15

print(f"O valor do imposto a pagar é: R$ {imposto:.2f}")

velocidade = float(input("Digite a velocidade atual do carro (em km/h): "))

if velocidade <= 80:
    print("Abaixo do limite de velocidade.")
else:
    multa = (velocidade - 80) * 5
    print(f"Multado! Você deverá pagar uma multa de R$ {multa:.2f}.")

    senha = input("Digite a senha: ")

if senha == "Python123":
    print("Acesso concedido.")
else:
    print("Acesso negado.")
