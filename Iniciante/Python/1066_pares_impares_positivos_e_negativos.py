#Creates variables with 0 value to increase it later 
pares = 0 
impares = 0 
positivos = 0 
negativos = 0
#Makes a 5x loop with conditionals to increese 1 to the variables every time the condition is reached 
for i in range (5):
    numero = int(input())
    if numero % 2 == 0: 
        pares += 1 
    else: 
        impares += 1 
    if numero > 0: 
        positivos += 1
    #elif here to deal with inputs (0), because it isn't a positive and even a negative number 
    elif numero < 0: 
        negativos += 1 
print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')