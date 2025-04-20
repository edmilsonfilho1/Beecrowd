casos = int(input())
total = 0 
coelhos = 0 
ratos = 0 
sapos = 0
#Makes a for range to receive a certain amount of inputs
for i in range (casos): 
    #This will get the numbers and the letters of the input 
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    #Atributes (quantidade) to (total)
    total += quantidade
    #Add 1 if the respective string is on the input
    if tipo == 'C':
        coelhos += quantidade
    if tipo == 'R': 
        ratos += quantidade
    if tipo == 'S': 
        sapos += quantidade
#Calculate de percentage of all 3 types of animals 
percoelhos = (coelhos/total) * 100
perratos = (ratos/total) * 100
persapos = (sapos/total) * 100
#Print it all 
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {percoelhos:.2f} %')
print(f'Percentual de ratos: {perratos:.2f} %')
print(f'Percentual de sapos: {persapos:.2f} %')
