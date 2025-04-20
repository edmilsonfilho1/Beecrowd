n = int(input())
#Makes a 10x loop to print i + 1 n times 
#We use i + 1 because the programms start by the position 0, so we add one to make the right multiplications
for i in range (10): 
    print(f'{i+1} x {n} = {(i+1)*n}')