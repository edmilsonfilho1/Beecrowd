#Creates variables with value 0 to atribute values inside the loop
alcool = 0 
gasolina = 0 
diesel = 0 
#Makes a loop that will make several inputs and check the conditions to make the additions, end the loop or restart it 
while True: 
    tipo = int(input())
    if tipo == 1: 
        alcool += 1
    elif tipo == 2:
        gasolina += 1 
    elif tipo == 3: 
        diesel += 1 
    elif tipo == 4: 
        break
    else: 
        continue
#Print it all 
print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}') 
