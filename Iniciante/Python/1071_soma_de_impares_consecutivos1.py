x = int(input())
y = int(input())
#Create a variable with value 0 to increase it later
soma = 0
#Makes x be the greatest one 
if x < y:
    x, y = y, x
#Makes the programm just use the number right after y 
y += 1
#While y<x soma will receive y, and y will receiva 1 every time   
while y < x:
    if y % 2 != 0:
        soma += y
    y += 1

print(soma)