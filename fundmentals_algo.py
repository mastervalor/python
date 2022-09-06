# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

for i in range(-300, 0):
    if i % -3 == 0:
        if i == -6:
            break
        print(i)

# Print integers from 2000 to 5280, using a WHILE.
x = 2000
while x <= 5280:
    print(x)
    x += 1

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for y in range(1,101):
    if y % 10 == 0:
        print('Dojo')
    elif y % 5 == 0:
        print('Ninja')
    else:
        print(y)
        
# Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

def flex_mult(low,high,mult):
    print(low, high, mult)
    for z in range(high+1, low, -1):
        if z % mult == 0:
            print(z)
            
flex_mult(2,9,3)