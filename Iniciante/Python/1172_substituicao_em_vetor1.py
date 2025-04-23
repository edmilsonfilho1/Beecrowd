#Makes a 10x for loop that will verify if x its null or negative

#If yes, it will change x to 1 

for i in range(10): 
    x = int(input())
    if x <= 0: 
        x = 1

    #Print the position and the number itself

    print(f'X[{i}] = {x}')