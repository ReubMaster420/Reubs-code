def power(a,b):
    if b == 0:
        return(1)
    elif a == 0:
        return(0)
    elif b == 1:
        return(1)
    else:
        return a*power(a,b-1)
print(power(3,5))