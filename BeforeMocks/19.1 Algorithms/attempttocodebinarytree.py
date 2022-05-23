NullPointer = -1 #Constant
RootPointer = 0 #Integer
FreePtr = 0 #Integer

class TreeNode:
    """
    This is the class that we use to make the record in Python.
    They'll probably want these to private too, but that takes us too far from the Pseudocode
    """
    def __init__(self):
        self.Data = 0.0 #float
        self.LeftPointer = -5 #Integer
        self.RightPointer = -1 #Integer had to do this to stop an error
    def __str__(self):
        return f"Left pointer {self.LeftPointer: >3}  Data {self.Data: >7}  Right Pointer {self.RightPointer: >3}"
        #Used f strings to make it easier to see what is going on.

Tree = [] # This is the 'array'
for i in range (7): Tree.append(TreeNode()) #This create the array to the size needed.

def InitiliseTree():
    """
    This Initialises the tree with 7 instances for the binary tree.
    To follow the pseudocode I need to use global variables liberally.
    """
    global NullPointer
    global RootPointer
    RootPointer = NullPointer
    FreePtr = 0
    for Index in range(6):
        Tree[Index].LeftPointer = Index + 1
    Tree[6].LeftPointer = NullPointer

def InsertNode(NewItem):
    """
    I've swapped the if FreePtr != NullPointer because Pycharm complained at me. Rightly so.
    The Hodder book was better here and so I raised an error if the array is full. Originally it just did nothing.
    If that's annoying change it to a print statement.
    """
    global FreePtr # Passed by ref
    global NullPointer # Passed by ref
    global RootPointer
    if FreePtr == NullPointer:
        raise Exception("Sorry, this binary Tree array is full")
    else:  # Space in the array
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr].LeftPointer
        Tree[NewNodePtr].Data = NewItem
        Tree[NewNodePtr].LeftPointer = NullPointer
        if RootPointer == NullPointer: # Check if empty tree
            RootPointer = NewNodePtr
        else:
            ThisNodePtr = RootPointer # Start at the root of the tree
            while ThisNodePtr != NullPointer:
                PreviousNodePtr = ThisNodePtr
                if Tree[ThisNodePtr].Data > NewItem:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr].LeftPointer
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr].RightPointer
            if TurnedLeft == True:
                Tree[PreviousNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer = NewNodePtr


def FindNode(SearchItem):
    """
    If it can't find the item then it will return -1.
    """
    global RootPointer
    global NullPointer
    ThisNodePtr = RootPointer
    while ThisNodePtr != NullPointer and Tree[ThisNodePtr].Data != SearchItem:
        if Tree[ThisNodePtr].Data > SearchItem:
            ThisNodePtr = Tree[ThisNodePtr].LeftPointer
            print("Went left",ThisNodePtr)
        else:
            ThisNodePtr = Tree[ThisNodePtr].RightPointer
            print("Went right",ThisNodePtr)
    return ThisNodePtr



InitiliseTree()

InsertNode(2.5)
InsertNode(5.7)
InsertNode(3.3)
InsertNode(7.5)
InsertNode(11.11)
InsertNode(12.4)
InsertNode(15.4)
#InsertNode(3.4)

for i in Tree: print(i)

print("found at location",FindNode(7.5))