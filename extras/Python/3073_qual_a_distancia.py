num1 = int(input())
num2 = int(input())
num3 = int(input())
#Math formula to find out the greatest number
maior_num1_num2 = (num1 + num2 + abs(num1-num2)) // 2 
maior_geral = (maior_num1_num2 + num3 + abs(maior_num1_num2-num3)) // 2 
#Math formula to find out the smallest number 
menor_num1_num2 = (num1 + num2 - abs(num1-num2)) // 2 
menor_geral = (menor_num1_num2 + num3 - abs(menor_num1_num2-num3)) // 2 
#shows up the greatest and the smallest number and subtract them
print(f'A distância entre o maior valor {maior_geral} e o menor valor {menor_geral} é {maior_geral-menor_geral}')
#Disclaimer: No conditional methods were allowed in this exercise 