import random
word_list = []
def importlist():
    try:
        with open("WordleList.txt","r") as f:
            for line in f:
                word_list.append(line.strip("\n"))
    except OSError:
        print("File NOT FOUND!")


def solverinput(array, word):
    possiblewords = []
    letterinword = []
    if array == ["","","","",""]:
        return random.choice(word_list)
    for i in range (5):
        if len(array[i]) >= 1:
            if array[i] not in letterinword:
                letterinword.append(array[i][:1])
                print(letterinword)
    for i in range (len(word_list)):
        templetter = letterinword
        for y in range(5):
            if word_list[i][y] in templetter:
                templetter.remove(word_list[i][y])
        if templetter == []:
            possiblewords.append(word_list[i])
    print("The possible words",possiblewords)
    return random.choice(possiblewords)


importlist()
wordoftheday = random.choice(word_list)
array = ["","","","",""]
starter = random.choice(word_list)
for i in range(5):
    word = solverinput(array, starter)
    starter = word
    word = solverinput(array, starter)
    print("The robot chose word:",word)
    for x in range(5):
        if word[x] in wordoftheday:
            array[x] = word[x]+"*"
        if word[x] == wordoftheday[x]:
            array[x] = word[x]
    if word == wordoftheday:
        print(array)
        print("Yeah you right")
        break
    print(array)
print("The word was",wordoftheday)
