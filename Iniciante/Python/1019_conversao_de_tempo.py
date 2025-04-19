#Receiving the seconds from user  
segundos = int(input())
#Converting seconds to hours  
horas = segundos // 3600 
#Making seconds receive the rest of the last division 
segundos %= 3600
#Converting what's left of seconds to minutes
minutos = segundos // 60 
#Making seconds receive the rest of the last division (again)
segundos %= 60 
print(f'{horas}:{minutos}:{segundos}')
