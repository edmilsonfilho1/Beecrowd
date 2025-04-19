#Receiving 3 int variables in the same line 
a, b, c = map(int, input().split())
#Creates 3 more variables to recibe the value of the original ones
a2 = a 
b2 = b 
c2 = c 
#Uses conditional structures to trasform (a) in the gratest and (c) in the smallest one 
#Need to use a temporary variable to keep the original value and chance to another variable if the condition its true 
if a < b: 
    t = a 
    a = b 
    b = t 
if a < c: 
    t = a 
    a = c 
    c = t 
if b < c: 
    t = b 
    b = c 
    c = t 
#Print it all 
print(c)
print(b)
print(a)
print()
print(a2)
print(b2)
print(c2)
