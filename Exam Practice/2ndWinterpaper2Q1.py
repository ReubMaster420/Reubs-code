from ast import Div


def Unknown(X,Y):
    if X < Y:
        print(X + Y,"ya")
        return (Unknown(X + 1, Y)*2)
    else:
        if X == Y:
            return (1)
        else:
            print(X + Y,"ya")
            return (Unknown(X-1,Y)// 2)
    
print("X:",10,"Y:",15)
print(Unknown(10,15))
    
print("X:",10,"Y:",10)
print(Unknown(10,10))
    
print("X:",15,"Y:",10)
print(Unknown(15,10))

def IterativeUnknown(X,Y):
    Total = 1
    while X != Y:
        print(str(X + Y))
        if X <Y:
            X = X + 1
            Total = Total * 2
        else:
            X = X -1 
            Total = int(Total/2)
    return Total

print("ITERATIVE --------------------------------------")
print("X:",10,"Y:",15)
print(IterativeUnknown(10,15))
    
print("X:",10,"Y:",10)
print(IterativeUnknown(10,10))
    
print("X:",15,"Y:",10)
print(IterativeUnknown(15,10))