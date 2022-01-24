import os


QueueData = ([" " for i in range(0,20)])
StartP = 0
EndP = 0

def Enqueue(DataToAdd, EndP):
    if(EndP == 20):
        return False,EndP
    else:
        QueueData[EndP] = DataToAdd
        EndP = EndP +1
        return True, EndP

def ReadFile(StartP,EndP):
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
print(ReadFile(StartP,EndP))

def Remove(StartP,EndP):
    if EndP - StartP >= 2:
        concatenated = str(QueueData[StartP])+str(QueueData[EndP])
        StartP = StartP + 2
        print(concatenated)
    else:
        print("No Items")




