Array = [179,6343, 62, 626, 64, 120, 26 , 1 , 5 , 3 ,250, 12]
top = len(Array)
swap = True #flag to stop loop if nothing in the list has been changed
while (swap) or (top>0): #if no swaps have occured or the top of the list has reduced to 0
    swap = False
    for i in range(top - 1): #length of the list
        if Array[i] > Array[i+1]: #if the lower index value is greater than the higher
            temp = Array[i] #put lower indes in temp
            Array[i] = Array[i+1] #replace lower index value with upper
            Array[i+1] = temp #place the temp value in upper
            swap = True #a swap has occured
    top = top -1 #reduce the length of the list to be swapped by 1 as top should be correct
print(Array)