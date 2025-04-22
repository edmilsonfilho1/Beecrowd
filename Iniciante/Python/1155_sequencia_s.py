#Creates variables to use in the loop 
num1 = 1
s = 0  
#Makes a loop that will add 1/num1 to (s), and add 1 to (num1) so all divisions can happen
for i in range (100):
    s += 1/num1
    num1 += 1
#Print it with 2 decimal houses
print(f'{s:.2f}')

