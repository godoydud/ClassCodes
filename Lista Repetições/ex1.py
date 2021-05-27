#Leia uma lista de 10 números reais e, em seguida, mostre-os na ordem inversa.

numeros = list(map(int, input("Digite os valores: ").split())) # Entrada dos 10 valores

cont = len(numeros) # Conta quantos valores foram digitados e guarda na variavel cont

for i in range(cont-1, -1, -1): # Contador subtrai 1 posição, pois temos um vetor de 5 posições(0, 1, 2, 3, 4) range com inicio em cont-1 e parada em -1, com intervalos de -1
    print(numeros[i], end=" ")


