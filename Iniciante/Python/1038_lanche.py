#Receiving 2 int variables in the same line 
codigo, quantidade = map(int, input().split())
#Creating the variable 'total' to show up the final result 
total = 0
#Using conditionals to calculate the final result   
if codigo == 1:
    total = quantidade * 4 
    print(f'Total: R$ {total:.2f}')
elif codigo == 2: 
    total = quantidade * 4.5 
    print(f'Total: R$ {total:.2f}')
elif codigo == 3: 
    total = quantidade * 5 
    print(f'Total: R$ {total:.2f}')
elif codigo == 4: 
    total = quantidade * 2
    print(f'Total: R$ {total:.2f}') 
else: 
    total = quantidade * 1.50 
    print(f'Total: R$ {total:.2f}')
