#creates a array
array = []

#Makes a 20x for loop that will receive several variables and put them at the array 
for i in range (20): 
    x = int(input())
    array += [x]
#It will reverse the array order 

array.reverse()

#Makes another 20x for loop to print each position and array 
for i in range(20): 
    print(f'N[{i}] = {array[i]}')

