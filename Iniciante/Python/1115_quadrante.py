#Creates variables to use in the future 
x = 1
y = 1
#Makes a boolean variable that verify if the loop should end  
fim = x == 0 or y == 0 
#Uses (fim) do start the loop
while not fim: 
    x, y = map(int, input().split())
    #Makes conditionals that verify witch number to print based on math rules
    if x > 0 and y > 0: 
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0: 
        print('terceiro')
    elif x > 0 and y < 0: 
        print('quarto')
    else: 
        break
