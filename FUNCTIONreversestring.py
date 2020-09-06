import random 
letter = ["a","b","c","d","e","f","g"]
word = random.choice(letter)
for i in range (random.randint(5,10)):
    word = word + random.choice(letter)
print ("The initial word is",word)

#reverse string
def reverse(word):
    word = word[::-1]
    return word
new = reverse(word)
print("Initial is",word,"reverse is",new)
