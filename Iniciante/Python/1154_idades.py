#Creates two variables with value 0 to increase in the loop

pessoas = 0
soma_idade = 0 

#Makes a loop what will receive (idade) and add it to (soma_idade) every time and add 1 to (pessoas) every time either 
#If the input its a negative number, the loop will end, and this number will not be considered a valid number in the operation
while True: 
    idade = int(input())
    if idade < 0: 
        break
    else:
        pessoas += 1 
        soma_idade += idade 
        continue
#Print it with 2 decimal houses
print(f'{(soma_idade/pessoas):.2f}')