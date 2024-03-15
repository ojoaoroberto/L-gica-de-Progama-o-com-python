qtdmax = int(input("Qual é a quantidade máxima? "))
qtdmin = int(input("Qual é a quantidade mínima? "))
qtdatual = int(input("Qual é a quantidade atual? "))


media = (qtdmax + qtdmin) / 2

if qtdatual >= media:
    print("Não precisa efetuar compra")

else:
    print("Precisa efetuar compra")