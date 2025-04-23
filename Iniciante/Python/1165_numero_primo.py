#Receive a value that we are gonna use in the for loop
casos = int(input())
#Creates a loop that will receive x input
for g in range (casos):
   x = int(input())
   soma = 0 
   #between the range 1-x, it will verify witch numbers x is divisible for 
   for i in range (1, x): 
      if x % i == 0: 
         soma += 1 
    #Verifies if the are more than two numbers that x is divisible for and them print the result 
   if soma < 2: 
     print(f'{x} eh primo')
   else: 
     print(f'{x} nao eh primo')