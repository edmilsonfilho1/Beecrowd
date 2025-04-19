#Receiving 3 float variables in the same line 
a, b, c = map(float, input().split())
#creating delta 
delta = (b**2 - 4 * a * c )
#Disclaimer: just square delta after make this verification 
#Otherwise it will turn into a complex number and the program will fail 
if delta < 0 or a == 0: 
    print('Impossivel calcular')
#Squaring delta, calculating x1 and x2 and printing them 
else: 
    delta = delta ** 0.5
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}') 