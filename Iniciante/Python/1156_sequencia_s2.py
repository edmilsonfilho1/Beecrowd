#Makes variables to use later in the loop 
s = 1 
num1 = 3 
num2 = 2
#Makes a loop that will add num1/num2 to s
#Every time it will add 2 to num1 and will double num2 (the logic used is based on the text of the exercise)
for i in range (19):
    s += num1/num2
    num1 += 2  
    num2 += num2
print(f'{s:.2f}')