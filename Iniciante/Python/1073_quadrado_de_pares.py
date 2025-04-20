n = int(input())
par = 0
#Verify if the number is even and use a while loop to show the even numbers 
if n % 2 == 0:
    while par < n:
        par += 2   
        print(f'{par}^{2} = {par**2}')
#put n-1 to cover operetations where n is a odd number 
else: 
    while par < n-1: 
        par += 2  
        print(f'{par}^{2} = {par**2}')

    