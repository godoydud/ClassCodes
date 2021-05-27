lista = list(map(int, input().split())) #Entrada
impar = [] #Instacia lista impar vazia
par = [] #Instancia lista par vazia

if len(lista) == 20: #Se tamanho da lista é 20

    for i in lista: #para i em lista
        if i % 2 == 0: #se resto da divisao de i por 2 é igual a 0
            par.append(i) #valores pares vao para a lista
        else:
            impar.append(i) #valores impares vao para a lista

    print("Lista: %s \n Impar: %s \n Pares: %s" %(lista, impar, par))