#Receiving for int variables in the same line 
a, b, c, d = map(int, input().split())
#Using conditionals and doing the requested comparations 
if b > c and d > a and c + d > a + b and c + d >= 0 and a % 2 == 0: 
    print('Valores aceitos')
else: 
    print('Valores nao aceitos')