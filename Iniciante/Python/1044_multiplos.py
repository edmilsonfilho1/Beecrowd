#Create 2 int variables in the same line 
a, b = map(int, input().split())
#Crete a boolean variable to check if the numbers are multiples
sao_multiplos = a % b == 0 or b % a == 0 
#Use conditional to see which message it should print 
if sao_multiplos == True: 
    print('Sao Multiplos')
else: 
    print('Nao sao Multiplos')