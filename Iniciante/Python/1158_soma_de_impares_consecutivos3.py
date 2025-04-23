#Receives the variable that we are gonna to use in the for loop

casos = int(input())

#Makes a for loop in (casos) range that will receive the input of (x) and (y)

for i in range (casos): 
    soma_impares = 0 
    x, y = map(int, input().split())

    #if (x) is a even number it will add 1 to him, so we get the odd numbers after it 
    if x % 2 == 0: 
        x += 1 
    
    #Makes a for loop that will verify if x its a odd number, if yes it will add (x) to (soma_impares)
    for i in range (y): 
        if x % 2 != 0: 
            soma_impares += x 
        x += 2 

    #Print (soma_impares)
    print(soma_impares)

