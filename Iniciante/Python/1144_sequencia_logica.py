casos = int(input())
#Create a variable with the initial value 
num = 1 
#For range that will print twice every time, num, num**2, num**3 
#The second print have num**2 and num**3 add 1, as the question wants
for i in range(casos): 
    print(num, num**2, num**3)
    print(num, num**2 + 1, num**3 + 1)
    num += 1