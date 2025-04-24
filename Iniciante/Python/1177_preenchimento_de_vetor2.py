t = int(input())
num = 0 

#Makes a for loop that will print the position (i) and (num)
#(Num) is 0 because we need the numbers between 0 and t - 1 
#Every time the loops happen num += 1, but if he turns equal to t it will turn to 0 again so the loop can keep going

for i in range(1000):
    print(f'N[{i}] = {num}')
    num += 1 
    if num == t:
        num = 0  

        

