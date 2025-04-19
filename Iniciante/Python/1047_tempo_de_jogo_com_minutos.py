h1, m1, h2, m2 = map(int, input().split())
#convert hours to minutes, making the whole operation way easier 
inicio = h1 * 60 + m1
fim = h2 * 60 + m2
#Make normal aritmetic operations
duracao = fim - inicio
if duracao <= 0:
    duracao += 24 * 60
#Convert minutes do hours at the end 
horas = duracao // 60
minutos = duracao % 60
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
 




