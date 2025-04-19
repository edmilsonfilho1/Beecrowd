renda = float(input())
#Creates a variable with value 0, that we are gonna use to atribuite the taxes
roubo = 0
#Now we just need to check the taxes list and print what is requested 
# Always remember: when passing through a certain tax bracket, the new percentage will only be applied to the amount that exceeded it
if renda <= 2000: 
    print('Isento')
elif renda <= 3000:
    roubo = (renda-2000) * 0.08
    print(f'R$ {roubo:.2f}')
elif renda <= 4500: 
    roubo = (1000*0.08) + (renda-3000) * 0.18
    print(f'R$ {roubo:.2f}')
else: 
    roubo = (1000*0.08) + (1500*0.18) + (renda-4500) * 0.28
    print(f'R$ {roubo:.2f}')

