n = int(input())
#Makes a variable with 1, we will increase it to check the numbers that n is divisible for
i = 1 
#Makes a for loop, while i <= n, it will check if the numbers are divisors of n 
#If they are, the loop will print it 
#Add 1 to i so the loop can keep goin 
while i <= n: 
    if n % i == 0: 
        print(i)
    i += 1 
