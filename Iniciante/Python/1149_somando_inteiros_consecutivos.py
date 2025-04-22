valores = list(map(int, input().split()))

A = valores[0]
N = 0

#It search the first n after a 
for valor in valores[1:]:
    if valor > 0:
        N = valor
        break

#Loop to pick up the N input every time he is equal or under 0 
while N <= 0:
    N = int(input())

#Add A + i until N-1
soma = 0
for i in range(N):
    soma += A + i

print(soma)