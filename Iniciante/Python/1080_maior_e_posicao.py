maior = 0 
posicao = 0
#Makes a 100x loop and use a conditional to store (numero) when its bigger than (maior)
for i in range (100): 
    numero = int(input())
    if numero > maior: 
        maior = numero
        posicao = (i+1)
#print it all 
print(maior)
print(posicao)
