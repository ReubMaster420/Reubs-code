list = [4,3,5,9,90,1,-4]

def insertion():
    for i in range(len(list)):
        currentvalue = list[i]
        j = i - 1
        while j >= 0 and currentvalue > list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = currentvalue

def bubble():
    swaps = True
    while swaps == True:
        swaps = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                temp = list [i]
                list[i] = list[i+1]
                list[i+1] = temp
                swaps = True
                print(list)
bubble()
