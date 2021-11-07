class Node:
    def __init__(self,DataValue, LeftPointer=None, RightPointer=None):
        self.DataValue = DataValue
        self.LeftPointer = LeftPointer
        self.RightPointer = RightPointer

BinaryTree = []

for i in range(0,12):
    BinaryTree.append(Node(0))

global NextNode
NextNode = 0

def CreateTree(NodeData):
    global NextNode
    BinaryTree[NextNode].DataValue = NodeData
    NextNode = NextNode + 1

def AttachLeft(NodeData, ParentNode):
    global NextNode
    BinaryTree[NextNode].DataValue = NodeData
    BinaryTree[ParentNode].LeftPointer = NextNode
    NextNode = NextNode + 1

def AttachRight(NodeData, ParentNode):
    global NextNode
    BinaryTree[NextNode].DataValue = NodeData
    BinaryTree[ParentNode].RightPointer = NextNode
    NextNode = NextNode + 1
    
startpointer = 0
def print_tree(BinaryTree, Pointer):
    while Pointer != None:
        print(BinaryTree[Pointer].DataValue)
        Pointer = BinaryTree[Pointer].LeftPointer

CreateTree("Red")
AttachLeft("Blue", 0)
AttachRight("Green", 0)
AttachRight("Black", 2)
AttachLeft("Brown", 2)
AttachLeft("Peach", 3)
AttachLeft("Yellow", 1)
AttachRight("Purple", 1)
AttachLeft("White", 6)
AttachLeft("Pink", 7)
AttachLeft("Grey", 9)
AttachRight("Orange", 9)


def counter(BinaryTree, Pointer):
    if BinaryTree[Pointer].LeftPointer == None and BinaryTree[Pointer].RightPointer == None:
        print(BinaryTree[Pointer].DataValue)
    elif BinaryTree[Pointer].LeftPointer:
        counter(BinaryTree,BinaryTree[Pointer].LeftPointer)
    elif BinaryTree[Pointer].RightPointer:
        counter(BinaryTree,BinaryTree[Pointer].RightPointer)

print(counter(BinaryTree, startpointer))

