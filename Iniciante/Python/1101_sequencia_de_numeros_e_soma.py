m = 1 
n = 1
#Create a loop that will receive inputs untill m <= 0 or n <= 0 
while m > 0 and n > 0:
    soma = 0 
    m, n = map(int, input().split())
    #End the loop if any number is equal or under 0 
    if m <=0 or n <=0: 
        break
    else:
        #Makes m be the greatest
        if m < n: 
            m, n = n, m 
        #Will store the numbers in the variable (soma)
        while m >= n:
            soma += n 
            #Print it all in the same line 
            print(n, end=' ')
            n += 1 
        print(f'Sum={soma}')



