horai, horaf = map(int, input().split())
#create two options of end game
fim1 = 24 - horai + horaf
fim2 = horaf - horai
if horai >= horaf: 
    print(f'O JOGO DUROU {fim1} HORA(S)')
else: 
    print(f'O JOGO DUROU {fim2} HORA(S)')