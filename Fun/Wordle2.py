
import random
word_list = []
def importlist():
    try:
        with open("WordleList.txt","r") as f:
            for line in f:
                word_list.append(line.strip("\n"))
    except OSError:
        print("File NOT FOUND!")
nullletters = []
letters = []
correctpletters = []
cletters = []
def solver(array, word):
    possiblewords = []
    if array == ["","","","",""]:
        return random.choice(word_list)
    else:
        for i in range(5):
            if len(array[i]) >= 1 and array[i][:1] not in letters:
                letters.append(array[i][:1])
            if array[i] == "" and word[i] not in nullletters:
                nullletters.append(word[i])
            if len(array[i]) == 1 and array[i] not in cletters:
                str1 = str(i)
                str2 = str(array[i])
                thing = str1 + str2
                correctpletters.append(thing)
                cletters.append(array[i])
    print("correct postions",correctpletters)
    print("Theses are the",nullletters)        
    print("Possible letters",letters)
    for i in range(len(word_list)):
        flag = True
        count = len(letters)
        for y in range(len(letters)):
            if letters[y] in word_list[i]:
                count = count - 1
        for y in range(5):
            if word_list[i][y] in nullletters:
                flag = False
        if count == 0 and flag == True:
            possiblewords.append(word_list[i])
            if correctpletters != []:
                for x in range(len(correctpletters)):
                    if correctpletters[x][1] != word_list[i][int(correctpletters[x][0])]:
                        try:
                            possiblewords.remove(word_list[i])
                        except:
                            print("")
                            
    #print("possible words are",possiblewords)
    return random.choice(possiblewords)

importlist()
wordoftheday = random.choice(word_list)
array = ["","","","",""]
starter = random.choice(word_list)
for i in range(6):
    print("List of letters:",letters)
    word = solver(array,starter)
    starter = word
    array = ["","","","",""]
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