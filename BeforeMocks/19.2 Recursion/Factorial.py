def factorial(number):
    if number == 0:
        answer = 1
    else:
        answer = number*factorial(number-1)
    return answer
print("0! =",factorial(0))
print("1! =",factorial(1))
print("2! =",factorial(2))
print("3! =",factorial(3))
print("4! =",factorial(4))
print("5! =",factorial(5))