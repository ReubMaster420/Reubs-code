#1a
class node:
    def __init__(self,data,nextnode):
        self.__data = data
        self.__nextnode = nextnode
    def data(self):
        return self.__data
    def next(self):
        return self.__nextnode

#1b
startpointer = 0
emptylist = 5
linkedlist = (node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1))

#1c
def outputNodes(linkedlist,currentpointer):
    while currentpointer != -1:
        print(linkedlist[currentpointer].data())
        currentpointer = linkedlist[currentpointer].next()
outputNodes(linkedlist,startpointer)

#1d)
def addNode(linkedlist,currentpointer,emptylist,dataadd):
    if emptylist<0 or emptylist>9:
        return False
    else:
        newNode = node(int(dataadd), -1)
        linkedlist[emptylist] = (newNode)
        previousPointer = 0
        while(currentPointer != -1):
            previousPointer = currentPointer
            currentPointer = linkedlist[currentPointer].next()
        emptyList = linkedlist[emptylist].next()
        return True

addNode(linkedlist, startpointer, emptylist, 12)
print("added data")
outputNodes(linkedlist,startpointer)


newarray = [node("","")]
newarray[0] = node(2,1)