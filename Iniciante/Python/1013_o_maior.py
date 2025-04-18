a, b, c = map(int, input().split())
if a < b: 
    t = a 
    a = b 
    b = t 
if a < c: 
    t = a 
    a = c 
    c = t 
print(f'{a} eh o maior')