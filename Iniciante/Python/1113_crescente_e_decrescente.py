#Create random variables values to use them in the future input
x = 1 
y = 2
#Using a while loop to receive the inputs and stop when x == y  
while x != y: 
    x, y = map(int, input().split())
    if x > y: 
        print('Decrescente')
    elif x < y: 
        print('Crescente')