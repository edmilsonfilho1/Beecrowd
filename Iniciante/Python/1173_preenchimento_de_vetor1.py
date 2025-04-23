#Makes the number input

num = int(input())

#Makes a for range that will print the (i) position, the number itself and will double the number every time, as requested.
for i in range (10):
    print(f'N[{i}] = {num}') 
    num = num * 2