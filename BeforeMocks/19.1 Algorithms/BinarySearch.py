Array = [1,2,4,6,7,8,19,29,36,74]

def binarysearch(find):
    upperbound = (len(Array)-1)
    lowerbound = 0
    while lowerbound <= upperbound:
        midpoint = int((upperbound+lowerbound)/2)
        if find == Array[midpoint]:
            return(midpoint)
        elif find < Array[midpoint]:
            upperbound = midpoint -1
        else:
            lowerbound = midpoint + 1 
    return("Not found")

print(binarysearch(500))
