casos = int(input())
for i in range(casos):
    a,b = 0,1
    x = int(input())
    for i in range(x): 
        a, b = b, a + b 
    print(f'Fib({x}) = {a}')