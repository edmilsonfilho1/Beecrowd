#Create a variable with value 0, that we will use to atribute values later 
pares = 0
#Makes a 5x loop to make 5 inputs and verify witch numbers are even 
#When it verifies that the number ir evenm it will increase 1 to (pares) 
for i in range (5): 
    numero = int(input())
    if numero % 2 == 0:
        pares += 1 
print(f'{pares} valores pares') 
