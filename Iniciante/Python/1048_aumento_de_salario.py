salario = float(input())
#Create boolean variables to every salary increase tax 
ajuste15 = salario <= 400
ajuste12 = salario <= 800
ajuste10 = salario <= 1200
ajuste7 = salario <= 2000
#Uses the boolean variables to make the calculus and print the information requested 
if ajuste15: 
    print(f'Novo salario: {salario*1.15:.2f}')
    print(f'Reajuste ganho: {salario*0.15:.2f}')
    print(f'Em percentual: {15} %')
elif ajuste12: 
    print(f'Novo salario: {salario*1.12:.2f}')
    print(f'Reajuste ganho: {salario*0.12:.2f}')
    print(f'Em percentual: {12} %')
elif ajuste10: 
    print(f'Novo salario: {salario*1.10:.2f}')
    print(f'Reajuste ganho: {salario*0.10:.2f}')
    print(f'Em percentual: {10} %')
elif ajuste7:    
    print(f'Novo salario: {salario*1.07:.2f}')
    print(f'Reajuste ganho: {salario*0.07:.2f}')
    print(f'Em percentual: {7} %')
else: 
    print(f'Novo salario: {salario*1.04:.2f}')
    print(f'Reajuste ganho: {salario*0.04:.2f}')
    print(f'Em percentual: {4} %')
