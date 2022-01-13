TheData = [29,3,4,8,12,99,4,26,4]

def insertion(list):
    for i in range(len(list)):
        DataToInsert = list[i]
        inserted = 0
        NextValue = i-1
        while NextValue >= 0 and  DataToInsert < list[NextValue]:
            if DataToInsert < list[NextValue]:
                list[NextValue + 1] = TheData[NextValue]
                NextValue -= 1
                list[NextValue + 1] = DataToInsert
            else:
                inserted += 1

def output(list):
    for i in range(len(list)):
        print(list[i])

#print("This is the data before using the insertion sort:")
#output(TheData)
#insertion(TheData)
#print("This is the data after using the insertion sort:")
#output(TheData)

def checker(number, list):
    if number in list:
        print("Found")
    else:
        print("Not Found")

checker(9, TheData)