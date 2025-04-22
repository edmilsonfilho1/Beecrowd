a = int(input())
b = 0
while True:
    b = int(input())
    if(b > a):
        break
soma = a
total = 1
while(soma < b):
    soma += a + total
    total += 1
print(total)
#Kind tired today guys, later i come back to explain this one 