
medias = [] # Instanciando vetor de médias
N = 2 # Número de alunos para calcular-se a média (Variável constante em MAIÚSCULO)
# ENTRADA E PROCESSAMENTO

# Leitura das notas dos 5 alunos
for i in range(N): # (0, 1, 2, 3, 4)
   # Cada aluno terá 4 notas

   somaNotas = 0
   print("Entre com as 4 notas do aluno %d: " %(i+1))
   
   somaNotas += float(input("Digite a nota 1: "))
   somaNotas += float(input("Digite a nota 2: "))
   somaNotas += float(input("Digite a nota 3: "))
   somaNotas += float(input("Digite a nota 4: "))

   medias.append(somaNotas/4) # Insere média no vetor médias

cont = 0 # Inicialização da variável contadora/incremento

# Temos o vetor de médias calculado

for media in medias:
   if media >= 7:
      cont += 1 # Variável contadora/incremento

# SAÍDA
print(cont)