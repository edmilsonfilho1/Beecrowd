n = int(input())
#Create a variable with 0 value to use in the while loop
divisor = 0
#Create a while loop that will check if divisor % n == 2, and print it if its right
while divisor < 10000:
    if divisor % n == 2: 
        print(divisor)
    #We add 1 to divisor out of the conditional to work normally
    #It will make the programm keep going 
    divisor += 1 