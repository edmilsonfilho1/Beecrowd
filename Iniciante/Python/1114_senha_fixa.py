#Create a variable with random value to use in the future 
senha = 0 
#Makes a while loop that will do a input and verify if its equal to 2002
while senha != 2002: 
    senha = int(input())
    if senha != 2002: 
        print('Senha Invalida')
    else: 
        print('Acesso Permitido')