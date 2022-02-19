arrayData = [10,5,6,7,1,12,13,15,21,8]

#bi
def linearsearch(num):
    flag = False
    for i in range (len(arrayData)):
        if arrayData[i] ==num:
            flag = True
    if(flag):
        print("The number was found")
    else:
        print("Number not found")
#num = int(input("Enter a number to see if its in the array:"))
#linearsearch(num)

#bii)
def bubblesort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData)-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
    
bubblesort()
print(arrayData)