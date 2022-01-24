list =  [179,6343, 62, 626, 64, 120, 26 , 1 , 5 , 3 ,250, 12]

def insertion(list):
    for i in range(len(list)):
        currentvalue = list[i] #This stores the current value in currentvalue
        j = i - 1 #specifies that j is the value under i
        while j >= 0 and currentvalue < list[j]: #makes sure the first run where j = -1 does not work and instead mores to j = 0, where the second part queies if the value above the j index is smaller
            list[j + 1] = list[j] #Value above j become j
            j = j - 1 #J gets decremented by 1
        list[j + 1] = currentvalue #if while was run then j becomes the current value and hence swapped
        print(list)

list =  [179,6343, 62, 626, 64, 120, 26 , 1 , 5 , 3 ,250, 12]

insertion(list)
