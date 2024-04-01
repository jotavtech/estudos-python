temperatura = float(input("Digite a temperatura atual (em °C): "))

if temperatura < 15:
    print("Está frio.")
elif 15 <= temperatura <= 25:
    print("Está ameno.")
else:
    print("Está quente.")