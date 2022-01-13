def Unknown(x,y):
    if x<y:
        print (x+y)
        return (Unknown(x+1,y)*2)
    else:
        if x == y:
            return (1)
        else:
            print(x+y)
            return int(Unknown(x - 1, y)/ 2)
print("Recursive Code:")
print("Return Value 10,15:", Unknown(10, 15))
print("Return Value 10,10:", Unknown(10, 10))
print("Return Value 15,10:", Unknown(15, 10))

def IterativeUnknown(x,y):
    number = 1
    while x != y:
        if x < y:
            number = number*2
            print(x+y)
            x = x + 1
        else:
            number = int(number/2)
            print(x+y)
            x = x - 1
    return number
print("Iterative Code:")
print("Return Value 10,15:", IterativeUnknown(10, 15))
print("Return Value 10,10:", IterativeUnknown(10, 10))
print("Return Value 15,10:", IterativeUnknown(15, 10))
