quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2
print("Quantidade média:", quantidade_media)

if quantidade_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")
