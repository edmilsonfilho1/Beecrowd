#Receiving the value from the user 
valor = float(input())
#Converting the value to cents, to make the math operations easier
# Use int to don't have problems with beecrowd formatation  
centavos = int(valor * 100)
#Converting the cents to the respective number wanted (100, 50, etc) 
cem = centavos // 10000
#Making cents be equal to the rest of the last division (this one and the fellow step will repeat several times here)
centavos %= 10000
cinquenta = centavos // 5000
centavos %= 5000 
vinte = centavos // 2000 
centavos %= 2000
dez = centavos // 1000 
centavos %= 1000 
cinco = centavos // 500 
centavos %= 500 
dois = centavos // 200 
centavos %= 200 
#moedas
um = centavos // 100 
centavos %= 100 
cinquentac = centavos // 50 
centavos %= 50
vintecincoc = centavos // 25  
centavos %= 25
dezc = centavos // 10 
centavos %= 10
cincoc = centavos // 5 
centavos %= 5
umc = centavos // 1 
centavos %= 1
#Printing it all 
print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinquenta} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')    
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{cinquentac} moeda(s) de R$ 0.50')
print(f'{vintecincoc} moeda(s) de R$ 0.25')
print(f'{dezc} moeda(s) de R$ 0.10')
print(f'{cincoc} moeda(s) de R$ 0.05')
print(f'{umc} moeda(s) de R$ 0.01')