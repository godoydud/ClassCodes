#Leia duas sequˆencias num´ericas de tamanho 10 cada. Apresente o resultado da da intercala¸c˜ao da
#primeira sequˆencia lida com a segunda e vice-versa.

s1 =[]
s2 = []
s3 = []
s4 = []

for i in range(3):
    s1.append(input())
    s2.append(input())

for i in range(3):
    s3.append(s1[i])
    s3.append(s2[i])
    s4.append(s2[i])
    s4.append(s1[i])

print(s3)
print(s4)

