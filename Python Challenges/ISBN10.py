total=0
multiplyer = [10,9,8,7,6,5,4,3,2]
while True:
    discount = int(input("input 9 digits:"))
    lol = list(map(int,str(discount)))
    if len(lol) == 9:
        checkdigit = lol[8]
        break
    else:
        print("Please input a 10-digit number")
for i in range (0,9):
    meow = lol[i]*multiplyer[i]
    total = total + meow
modulo11 = total%11
modulo11tru = 11 - modulo11
print (modulo11tru)
