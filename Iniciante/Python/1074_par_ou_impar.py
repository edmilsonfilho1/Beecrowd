n = int(input())
#Makes a loop to make several inputs based on the variable (n)
for i in range (n):
    value = int(input())
    #Creates boolean variables to check the type and sinal of the number 
    even = value % 2 == 0 
    odd = value % 2 != 0    
    positive = value > 0 
    negative = value < 0 
    null = value == 0  
    #Uses the variables to print the right text 
    if even and positive: 
        print('EVEN POSITIVE')
    elif even and negative: 
        print('EVEN NEGATIVE')
    elif odd and positive: 
        print('ODD POSITIVE')
    elif odd and negative: 
        print('ODD NEGATIVE')
    else: 
        print('NULL')
 
