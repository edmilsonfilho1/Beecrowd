n = int(input())
fatorial = 1
#Makes a for range that will multiplicate n *(n-1) until it be 0 
for i in range (1, n+1): 
    fatorial = fatorial * i
print(fatorial)