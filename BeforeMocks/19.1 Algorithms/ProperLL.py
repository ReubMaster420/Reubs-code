class listnode:
    def __init__(self, data, pointer = None):
        self.data = data
        self.pointer = pointer

    def printme(self):
        x = [self.data, self.pointer]
        print (x)

def printLL():
    for i in LL:
        try:
            i.printme()
        except AttributeError:
            print ([None,None])

#create a linked list
LL = []
SP = None #initialise start pointer

def additem(newitem):
    global SP
    if SP == None:
        LL.append(listnode(newitem))
        SP = 0
    else:
        pointer = SP
        while LL[pointer].pointer != None: #goes through each node until the next is none
            pointer = LL[pointer].pointer
        LL.append(listnode(newitem))
        LL[pointer].pointer = len(LL)-1 #makes the previous pointer point to the new item

def removeitem(val):
    global SP
    if SP == None: #checks if the list is empty
        print ("list is empty, nothing to remove")
    next = SP
    if LL[next].data == val: #checks to see if its the first value
        SP = LL[next].pointer
        LL[next] = None
    else:
        found = False
        prev = next
        next = LL[next].pointer
        while not found:
            if LL[next].data == val: #if value found 
                LL[prev].pointer = LL[next].pointer #makes the previous pointer the pointer for the one ahead (so JUMP)
                LL[next] = None #makes the value of the None
                found = True
            elif LL[next].pointer is not None: #if not at the end of the linked list yet
                prev = next #updates the pointers by 1
                next = LL[next].pointer
            else:
                print ("not in linked list") #if value still not found and got to none item is not in the linked list

additem("Nushie")
printLL()
print("-------------------------------------------------------------")
additem("Kellie")
printLL()
print("-------------------------------------------------------------")
additem("Scarlett")
printLL()
print("-------------------------------------------------------------")
removeitem("Kellie")
printLL()
print("-------------------------------------------------------------")
additem("John")

printLL()