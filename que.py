class Node:
    def __init__(self, data, pointer=None):
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

LL = []
SP = None

def additem(newitem):
    global SP
    if SP == None: #list is empty
        LL.append(Node(newitem))
        SP = 0 #shows that there is data in the index 0
    else:
        pointer = SP
        while LL[pointer].pointer != None:
            pointer = LL[pointer].pointer
        LL.append(newitem) #adds a new item to the list
        LL[pointer].pointer = len(LL)-1 #makes the pointer before the new item point to it

def removeitem(val):
    global SP
    if SP==None: #list is empty
        print("No item to remove the list is empty")
    next = SP
    if LL[next].data == val:#checks to see if its the first value
        SP = LL[next].pointer
        LL[next] = None
    if LL

