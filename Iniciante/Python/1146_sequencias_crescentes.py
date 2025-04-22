#Makes a loop that will receive several inputs
while True:
    #Restarts the value of y 
    y = 1 
    x = int(input())
    #for loop that will print y xtimes and add 1 to y every time, so we get all the numbers between 1 and x 
    for i in range(x): 
        print(y, end="\n" if y % x == 0 else " ")
        y += 1 
    #If x == it will end the loop, otherwhise it will repeat it 
    if x == 0: 
        break
    else: 
        continue

