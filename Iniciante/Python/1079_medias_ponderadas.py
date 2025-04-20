casos = int(input())
#Use a for range to map 3 float variables and calculate the weighted average
for i in range (casos): 
    caso1, caso2, caso3 = map(float, input().split())
    media_ponderada = (caso1 * 2 + caso2 * 3 + caso3 *5) / 10 
    print(f'{media_ponderada:.1f}')
