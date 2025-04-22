x, y = map(int, input().split())
num = 1 
while y >= num: 
    for i in range (x):
        #it will break the line when x  numbers are printed in the same line
        print(num, end="\n" if num % x == 0 else " ")
    num += 1
