#Receiving 4 float variables in the same line 
nota1, nota2, nota3, nota4 = map(float, input().split())
#Creating the first media 
media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) / 10
#Printing the first media  
print(f'Media: {media:.1f}')
#Using conditionals to see if the student is aproved or not, and printing the requested
if media >= 7: 
    print('Aluno aprovado.')
elif media < 5: 
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    nota5 = float(input())
    print(f'Nota do exame: {nota5:.1f}')
    mediaf = (nota5 + media) / 2
    if mediaf >= 5: 
        print('Aluno aprovado.')
        print(f'Media final: {mediaf:.1f}')
    else: 
        print('Aluno reprovado.')
        print(f'Media final: {mediaf:.1f}')
