import os


QueueData = ([" " for i in range(0,20)])
startpointer = 0
endpointer = 0

def Enqueue(item):
    Flag = False
    for i in range(len(QueueData)):
        if QueueData[i] == (" ") and Flag == False:
            QueueData[i] = item
            Flag = True
    return (Flag)

def ReadFile():
    value = 0
    filenname = input("Enter a file name: ")
    try:
        with open("filename","r") as whole_file:
            for line in whole_file:
                Enqueue(line)
                if Enqueue(line) == False:
                    value = 1
                else:
                    value = 2
    except OSError:
        print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is", os.getcwd())
        value = -1

    if value == 2:
        print("All items were added to the Queue")
    elif value == 1:
        print("The queue was full")
    return value

print(ReadFile())



