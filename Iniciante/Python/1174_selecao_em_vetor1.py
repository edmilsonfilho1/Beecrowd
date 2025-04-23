#Makes a 100x for loop that will receive several inputs and verify if its equal or smallest than 10, and right after print it 

for i in range(100): 
    x = float(input())
    if x <= 10:
        print(f'A[{i}] = {x:.1f}')