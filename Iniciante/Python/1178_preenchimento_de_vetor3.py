x = float(input())

#Makes a loop that will print the position and the number, and will divide the number by 2 every time
#Remeber to use :.4f to print the first 4 decimal houses
for i in range (100): 
    print(f'N[{i}] = {x:.4f}')
    x = x/2