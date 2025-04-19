#Creates a variable that will store the number of positive numbers 
positivos = 0
#Makes a range loop that will receive a variable 6 times and make a verification to see if its a even number or not
#Every time (valor) receive a even number the programm will add 1 to the variable (positivos)
for i in range(6): 
    valor = float(input())
    if valor > 0:
        positivos += 1
print(f'{positivos} valores positivos')  
