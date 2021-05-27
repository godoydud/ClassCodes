# Leia 11 números inteiros e, em seguida, calcule a média destes números.

numeros = list(map(int, input().split()))

soma = 0
if len(numeros) == 11:
    for num in numeros:
        soma = soma + num
    media = soma/len(numeros)
    print("A média entre os números %s é %.f" %(numeros, media))
else:
    print("Erro")

