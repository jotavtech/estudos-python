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


