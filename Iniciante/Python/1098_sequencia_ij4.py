i = 0
#it will make the for range to print the 3 results wanted every time 

while i <= 2:
    #Restart the value of j 
    j = 1
    for _ in range(3):
        #Adding j+i to the final result to gets the right answer 
        print(f'I={i:.1f} J={(j + i):.1f}')
        #Increases j in one every time in the for loop  
        j += 1
    #Increses i in 0.2 until the end of the while loop 
    i += 0.2


