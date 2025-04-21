vitoria_inter = 0 
vitoria_gremio = 0 
grenais = 0 
empates = 0 
#Creates a while loop that will increase (grenais) in 1 every time it happens

while True: 
    grenais += 1 
    gols_inter, gols_gremio = map(int, input().split())
    #test which footbal team had more goals in the match, the one with more will have (vitoria_x) variable increased in one 
    if gols_inter > gols_gremio: 
        vitoria_inter += 1 
    elif gols_gremio > gols_inter:
        vitoria_gremio += 1 
    else: 
        #Gets the draw numbers 
        empates += 1 
    #Aks if the user wants to restart the programm 
    novo_grenal = int(input('Novo grenal (1-sim 2-nao)\n'))
    if novo_grenal == 1: 
        #restart the programm
        continue
    else: 
        #End the program 
        break
#Print the requested outputs
print(f'{grenais} grenais')
print(f'Inter:{vitoria_inter}')
print(f'Gremio:{vitoria_gremio}')
print(f'Empates:{empates}')
#Verify which footbal team have win more 
if vitoria_inter > vitoria_gremio: 
    print('Inter venceu mais')
elif vitoria_gremio > vitoria_inter: 
    print('Gremio venceu mais')
