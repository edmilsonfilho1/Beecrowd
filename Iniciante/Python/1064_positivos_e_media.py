#Create to variables with value 0 to atribuite values in the future
positivos = 0 
soma = 0
#Makes a 6x loop with a conditional that will increase (positivos) and (soma) 
for i in range (6): 
    numero = float(input())
    if numero > 0: 
        positivos += 1 
        soma += numero
#calculates the amount of positive numbers divided by it amount
media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')    