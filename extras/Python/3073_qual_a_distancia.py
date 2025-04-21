num1 = int(input())
num2 = int(input())
num3 = int(input())
#Makes num1 the greatest one 
if num1 < num2: 
    num1, num2 = num2, num1
if num1 < num3: 
    num1, num3 = num3, num1
#Makes num3 the smallest one 
if num2 < num3: 
    num2, num3 = num3, num2
#shows up the greatest and the smallest number and subtract them
print(f'A distância entre o maior valor {num1} e o menor valor {num3} é {num1-num3}')
