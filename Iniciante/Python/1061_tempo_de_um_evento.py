#Manipulate the variable spliting it, choosing the site after the backspace to convert to int 
dia_i = int(input().split()[1])
#It also split the variables, dividing them by " : ", so we just get the numbers between
x1, y1, z1 = map (int, input().split(' : '))
dia_f = int(input().split()[1])
x2, y2, z2 = map(int, input().split(' : '))
#Convert it all to seconds 
segundos_i = dia_i * 86400 + x1 * 3600 + y1 * 60 + z1
segundos_f = dia_f * 86400 + x2 * 3600 + y2 * 60 + z2
#Create the total seconds 
total = segundos_f - segundos_i
#Calculate days, hours, minutes and seconds
dias = total // 86400
total %= 86400
horas = total // 3600
total %= 3600
minutos = total // 60 
total %= 60 
segundos = total 
#print it all 
print(f'{dias} dia(s)') 
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')

