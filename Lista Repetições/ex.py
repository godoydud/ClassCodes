
#n = []
#n = list(input("Insira um número de dois algarismos ou mais: "))

#N = len(n)

#if n[0] == n[N-1]:
#    print(True)
#else:
#    print(False)
    
d = []
n = int(input())
casas = len(str(n))

divisor = 10


while n+1 > casas-(casas-1):
  d.append(n%divisor)
  n = n //divisor
print(d[::-1])

print('\n')

if d[0] == d[casas-1]:
    print("Igual")
else:
    print("Falso")