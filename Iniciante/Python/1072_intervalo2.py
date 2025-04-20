n = int(input())
#Create 2 variables with 0 value to increase in the loop later
dentro = 0 
fora = 0
#Make a loop in the range of the variable (n)
#Makes a verification every time to se if the number is between the intervals
# if positive, (dentro) will increase 1, otherwise, (fora) will increase 1  
for i in range (n): 
    x = int(input())
    intervalo = (x >= 10) and (x <= 20)
    if intervalo:
        dentro += 1 
    else: 
        fora += 1 
#Print it all 
print(f'{dentro} in')
print(f'{fora} out')


