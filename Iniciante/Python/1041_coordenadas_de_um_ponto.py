#Creating 2 float variables in the same line 
x, y = map(float, input().split())
#Using conditional to get the location of the points 
#For aditional doubts, search for geometry articles to see the rules used here 
if x == 0 and y == 0:
           print('Origem')
elif x > 0 and y > 0:
           print('Q1')
elif x < 0 and y > 0:
           print('Q2')
elif x < 0 and y < 0:
           print('Q3')
elif x > 0 and y < 0:
           print('Q4')
elif y == 0: 
    print('Eixo X')
elif x == 0: 
    print('Eixo Y')