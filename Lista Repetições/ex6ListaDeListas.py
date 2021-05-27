medias = [] # Média de todos os alunos
notas = [] # Notas de todos os alunos

N = 2

for i in range(N):
   notasAluno = []
   print("Informe as notas do aluno %d: " %(i+1))

   for j in range(4):
      nota = float(input("Digite a nota %d: " %(j+1)))
      notasAluno.append(nota)
   
   notas.append(notasAluno)
   medias.append(sum(notasAluno)/4)

cont = 0

for media in medias:
   if media >= 7:
      cont += 1

for i in range(N):
   print("Notas do aluno %d: " %(i+1), end = " ")
   print(notas[i])
   
print(cont)
