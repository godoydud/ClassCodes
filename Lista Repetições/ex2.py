#  Leia 4 notas e, em seguida, apresente as notas lidas bem como a médias das mesmas.

notas = list(map(float, input().split())) # Entrada

soma = 0 # Variável para guardar resultados de soma

for nota in notas:
    soma = soma + nota # Soma recebe 0 + nota + nota + nota + nota

media = soma/len(notas) # Média recebe soma das notas dividido pelo número de notas digitadas

print("Notas: %s \n Média %s" %(notas, media))




