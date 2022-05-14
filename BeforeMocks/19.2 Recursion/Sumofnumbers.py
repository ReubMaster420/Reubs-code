numbers = [4,5,7,8,0,3]

def sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])


print(sum(numbers))
