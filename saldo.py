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