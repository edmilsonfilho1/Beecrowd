casos = int(input())

#Makes a for loop that will receive the (x) input 

for i in range (casos): 
    perfeito = 0 
    x = int(input())

    #In the range (1, x) it will verify if there are numbers that are x is divisible for, and add this numbers to the variable (perfeito)

    for i in range(1, x):
        if x % i == 0: 
            perfeito += i
            
    #It verifies if (perfeito) is equal to x, if yes, the numbers is perfect, otherwise it isn't 

    if perfeito == x: 
        print(f'{x} eh perfeito')
    else: 
        print(f'{x} nao eh perfeito')
 
        

