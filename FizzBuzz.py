number = []
for count in range (1,21):
    if count%3 == 0 and count%5 == 0:
        number.append("fizzbuzz")
    elif count%3 == 0:
        number.append("fizz")
    elif count%5 == 0:
        number.append("buzz")
    else:
        number.append(count)
print(number)
    
