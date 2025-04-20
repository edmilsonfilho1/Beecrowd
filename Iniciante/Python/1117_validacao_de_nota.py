#Make a loop to verify if the grade is valid or not 
while True: 
    nota1 = float(input())
    if nota1 > 10 or nota1 < 0: 
        print('nota invalida')
    else: 
        #atribuites nota1 to media and stop the loop right after
        media = nota1
        break
#Another verification loop 
while True: 
    nota2 = float(input())
    if nota2 > 10 or nota2 < 0: 
        print('nota invalida')
    else: 
        media += nota2
        break
#Print it all with 2 numbers after the point 
print(f'media = {(media/2):.2f}')

