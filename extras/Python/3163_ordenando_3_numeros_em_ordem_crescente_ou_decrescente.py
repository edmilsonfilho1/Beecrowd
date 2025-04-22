n1 = int(input())
n2 = int(input())
n3 = int(input())
#Makes n1 be the greatest 
if n1 < n2: 
    n1, n2 = n2, n1
if n1 < n3: 
    n1, n3 = n3, n1
#Makes n3 be the smallest
if n2 < n3: 
    n3, n2 = n2, n3 
#Makes a input of a str type variable
tipo = str(input())
#Verify the variable to check which message it should pint
if tipo == 'CRESCENTE': 
    print(f'{n3} <= {n2} <= {n1}')
elif tipo == 'DECRESCENTE': 
    print(f'{n1} >= {n2} >= {n3}')