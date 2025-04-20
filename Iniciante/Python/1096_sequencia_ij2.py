i = 1 
j = 7 
#Makes a while loop to take -1 form j, and when j == 4 it turns back to 7 
while j >= 5: 
    print(f'I={i} J={j}')
    j += -1 
    if j == 4: 
        j = 7 
        #add 2 to (i) to keep the sequence
        i += 2 
        if i > 10:
            #Makes the loop stop when i bigger than 10, so it will print until 9  
            break