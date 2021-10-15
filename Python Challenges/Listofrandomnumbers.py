import random
number = []
Maximum = 0
Minimum = 1000
sum = 0
for i in range (0,50):
    number.append(random.randint(0,100))
for i in range (0,50):
    if number[i] > Maximum:
        Maximum = number[i]
    elif number[i] < Minimum:
        Minimum = number[i]
    sum = sum + number[i]
average = sum/50
print (Maximum,Minimum,average)
