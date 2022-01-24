Array = [1,2,4,6,7,8,19,29,36,74]
def binarysearch(find):
    found = False
    runs = 0
    upperbound = (len(Array)-1)
    lowerbound = 0
    while found == False and upperbound != lowerbound:
        runs = runs + 1
        midpoint = int((upperbound+lowerbound)/2)
        if find == Array[midpoint]:
            found = True
        if find > Array[midpoint]:
            lowerbound = midpoint 
        if find < Array[midpoint]:
            upperbound = midpoint 
    if(found):
        print("item found after",runs,"runs")
    else:
        print("no")

binarysearch(500)
