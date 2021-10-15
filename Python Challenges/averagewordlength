document = input("Copy and paste a text file:")
length = []
count = 0
for i in range (len(document)):
    if document[i] == ' ':
        length.append(count)
        count = 0
    else:
        count = count + 1
length.append(count)
average = sum(length)/len(length)
print ("Average word length is", average)
