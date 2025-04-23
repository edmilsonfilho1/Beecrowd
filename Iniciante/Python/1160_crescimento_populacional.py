casos = int(input())

#Makes a for loop in (casos) range that will receive the inputs and make (pa) and (pb) int and (g1) and (g2) float

for i in range(casos): 
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    anos = 0

    #Males a while loop that will increase de growing rate to (pa) and pb
    #Every time this loop happens, anos will receive 1 
    while pa <= pb:
        pa += int(pa * g1 / 100)
        pb += int(pb * g2 / 100)
        anos += 1

        #If anos > 100 it will print "mais de 1 seculo" and stop the programm
        
        if anos > 100:
            print("Mais de 1 seculo.")
            break

    if anos <= 100:
        print(f"{anos} anos.")