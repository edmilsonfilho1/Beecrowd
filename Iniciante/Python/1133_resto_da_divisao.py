x = int(input())
y = int(input())
#Makes x the greatest
if x < y: 
    x,y = y,x 
#Makes a loop that will check the condition several times and print it if attends to the condition 
#Y receives 1 to make the verification between it and x 
#Put x > y and y+= 1 because we shouldn't consider the numbers of the variable itself
y += 1 
while x > y: 
    resto_2_ou_3 = (y % 5== 2) or (y % 5 == 3)
    if resto_2_ou_3: 
        print(y)
    y += 1 

