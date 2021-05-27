d = []

# n tem 7 dígitos
n = int(input())
N = len(n)
divisor = 10

for i in range(N-1):
    d[i] = n % divisor
    n = n // divisor

for i in range(6, -1, -1):
  print(d[i], end =' ')

