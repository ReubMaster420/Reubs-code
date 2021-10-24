import math
yes = int(input("Enter a number:"))
primearray = []
numb = math.ceil(0.5*yes)+1
for i in range (2,numb):
    if yes%i == 0:
        primearray.append(i)
if primearray == []:
    print (yes,"is a prime number")
else:
    print (yes,"isnt a prime number and is divisible by",primearray)