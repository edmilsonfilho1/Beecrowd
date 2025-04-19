animal = str(input())
#Not much to talk in this one, we just need to make several conditionals to print the right value
if animal == 'vertebrado':
    animal = str(input())
    if animal == 'ave': 
        animal = str(input())
        if animal == 'carnivoro': 
            print('aguia')
        else: 
            print('pomba')
    else: 
        animal = str(input())
        if animal == 'onivoro': 
            print('homem')
        else: 
            print('vaca')
else: 
    animal = str(input())
    if animal == 'inseto': 
        animal = str(input())
        if animal == 'hematofago': 
            print('pulga')
        else: 
            print('lagarta')
    else: 
        animal = str(input())
        if animal == 'hematofago': 
            print('sanguessuga')
        else: 
            print('minhoca')

