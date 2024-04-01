velocidade = float(input("Digite a velocidade atual do carro (em km/h): "))

if velocidade <= 80:
    print("Abaixo do limite de velocidade.")
else:
    multa = (velocidade - 80) * 5
    print(f"Multado! Você deverá pagar uma multa de R$ {multa:.2f}.")