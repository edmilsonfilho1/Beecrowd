a, b , c = map(float, input().split())
#Uses a temporary variable to turn (a) into the greater one 
if a < b: 
    t = a 
    a = b 
    b = t 
if a < c: 
    t = a 
    a = c 
    c = t 
#Creates bool variables to test differents triangle types 
nao_triangulo = a >= b + c 
retangulo = a**2 == b**2 + c**2 
obtusangulo = a**2 > b**2 + c**2
acutangulo = a**2 < b**2 + c**2
equilatero = a == b == c 
isosceles = (a == b and b != c) or (b == c and c != a) or (c == a and a != b)
#Causes triangle types to be tested only if they actually are triangles
if nao_triangulo == False: 
    if retangulo: 
        print('TRIANGULO RETANGULO')
    if obtusangulo: 
        print('TRIANGULO OBTUSANGULO')
    if acutangulo: 
        print('TRIANGULO ACUTANGULO')
    if equilatero: 
        print('TRIANGULO EQUILATERO')
    if isosceles: 
        print('TRIANGULO ISOSCELES')
else: 
    print('NAO FORMA TRIANGULO')