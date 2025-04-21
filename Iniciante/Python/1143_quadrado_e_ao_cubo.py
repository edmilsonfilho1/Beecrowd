casos = int(input())
#Create a variable with the initial value needed
num = 1 
#Create a for loop in (casos) range that will print num, num**2 and num**3
#After that, it will increase 1 to num, so the loop will use the numbers after it 
for i in range(casos):
    print(num, num**2, num**3) 
    num += 1
