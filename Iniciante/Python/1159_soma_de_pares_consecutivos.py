while True:
    soma_par = 0  

    #Receives the input and stop the loop if x == 0 

    x = int(input())
    if x == 0:
        break
    
    #If x its a odd number it will add 1 to it and be a even number
    if x % 2 != 0:
        x += 1

    #Makes a 5x for range that will add (x) to (soma_par) if it is a even number

    for i in range(5): 
        if x % 2 == 0: 
            soma_par += x 
        
        #X += 2 every time so the programm can keep going 
        x += 2 

    print(soma_par)

        
