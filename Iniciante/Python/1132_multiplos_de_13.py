x = int(input())
y = int(input())
soma = 0 
#Makes x the bigger
if x < y: 
    x,y = y,x
#Makes a loop that will check if y its divisible by 13, increasing 1 to him every loop 
while x >= y: 
    if y % 13 != 0: 
        soma += y
    y += 1 
#Print the result
print(soma)