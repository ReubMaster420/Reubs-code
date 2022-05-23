class node:
    def __init__(self,data,pointer=None):
        self.data = data
        self.pointer = pointer

def displayLL():
    for i in range(len(LL)):
        print(LL[i].data,'    ',LL[i].pointer)

SP = None
LL = []

def addnode(data):
    global SP
    if SP == None:
        LL.append(node(data))
        SP = 0
    else:
        pointer = SP
        while LL[pointer].pointer != None:
            pointer = LL[pointer].pointer
        LL.append(node(data))
        LL[pointer].pointer = len(LL) -1
        
def deletenode(val):
    global SP
    if SP == None:
        print(1)
        return("List is empty cannot delete")
    next = SP
    if LL[next].data == val:
        LL[SP] = None
        SP = None
    else:
        prev = next
        found = False
        next = LL[next].pointer
        while not found:
            if LL[next].data == val:
                LL[prev].pointer = LL[next].pointer
                LL[next].data = None
                LL[next].pointer = None
                found = True
            elif LL[next].pointer != None:
                prev = next
                next = LL[next].pointer
            else:
                print("Not in list")

addnode("Chris")
addnode("Abdul")
addnode("Inshallah")
displayLL()
deletenode("Abdul")
displayLL()