while True: 
    media = 0 
    nota1 = float(input())
    while nota1 > 10 or nota1 < 0: 
        print('nota invalida')
        nota1 = float(input())
    media += nota1

    nota2 = float(input())
    while nota2 > 10 or nota2 < 0: 
        print('nota invalida')
        nota2 = float(input())
    media += nota2
    print(f'media = {(media/2):.2f}')
    novo_calculo = int(input('novo calculo (1-sim 2-nao)\n'))
    while novo_calculo < 1 or novo_calculo > 2 :
         novo_calculo = int(input('novo calculo (1-sim 2-nao)\n'))
    if novo_calculo == 2: 
        break
#Kind tired to add the explanation right now, soon i come back to add it 
            

