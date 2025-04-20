casos = int(input())
#Makes a for loop to receive several inputs 
for i in range (casos): 
    x, y = map(int, input().split())
    #Makes x be the greates
    if x < y: 
        x, y = y, x
    soma = 0 
    #Will not consider y, because we just need the numbers between them
    y += 1 
    #When y < x it will increase the value of y to (soma)
    #Will add 1 to y every time the loop happens
    while y < x: 
        if y % 2 != 0:
            soma += y
        y += 1
    print(soma)


