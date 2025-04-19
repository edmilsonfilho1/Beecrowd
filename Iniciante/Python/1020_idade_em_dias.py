#Receiving the days from the user 
dias = int(input())
#Converting days to years 
anos = dias // 365
#Making days be equal to the rest of the last division  
dias %= 365
#Converting days to months 
meses = dias // 30 
#Making days be equal to the rest of the last division 
dias %= 30
#Printing the variables 
print(f'{anos} ano(s)') 
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')