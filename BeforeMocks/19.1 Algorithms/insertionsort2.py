list =  [179,6343, 62, 626, 64, 120, 26 , 1 , 5 , 3 ,250, 12]

def insertion():
    for i in range(len(list)):
        currentvalue = list[i]
        j= i -1                #2 things after range
        while j>= 0 and list[j] > currentvalue:
            list[j+1]= list[j]
            j = j - 1                    #2 things after while
        list[j+1] = currentvalue                #final j+1 = initial thing