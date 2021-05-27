#Leia as informa¸c˜oes de idades e alturas de 30 pessoas. Determine quantas pessoas com mais de 13
#anos possuem altura inferior a m´edia das alturas.

idades = []
alturas = []
cont = 0

for i in range(5):
    idades.append(int(input("Insira idade da pessoa %d: " %(i+1))))
    alturas.append(int(input("Insira altura da pessoa %d (em centímetros): " %(i+1))))


media = (sum(alturas)/5)

for i in range(5):
    if idades[i] > 13:
        if alturas[i] < media:
           cont += 1

print("Temos %d pessoa(s) acima de 13 anos que possuem altura média inferior à %d cm" %(cont, media))
        
   

