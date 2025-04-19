#Recives 3 float variables in the same line 
a, b, c = map(float, input().split())
#Create a bool variable that tell us if a triangle will exist or not 
nao_triangulo = (a + b <= c) or (a + c <= b) or (b + c <= a)
#Uses a conditional and the bool variable to check if the programm shows 'area' or 'perimetro'
if nao_triangulo == True: 
    area = ((a+b) * c) / 2
    print(f'Area = {area:.1f}') 
else: 
    perimetro = a + b + c 
    print(f'Perimetro = {perimetro:.1f}')

