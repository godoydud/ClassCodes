numeros = list(map(int, input().split())) # Entrada de dados

soma = 0 # Seta as variáveis em 0
qntd = 0
for num in numeros: 
    soma = soma + num # Soma recebe soma + num digitado

media = soma/len(numeros) # Calculo da média, soma dividido pela quantidade de números digitados

for num in numeros:
    if num < media: # Se o numero digitado for menor que a média
        qntd += 1 # Soma-se +1 na variável quantidade

print(media)
print("Temos %d notas menores que a média." %(qntd))





