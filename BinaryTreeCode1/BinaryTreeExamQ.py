class Node:
    def __init__(self,DataValue, Left=None, Right=None):
        self.DataValue = DataValue
        self.LeftPointer = Left
        self.RightPointer = Right

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
    BinaryTree[ParentNode].Left = NextNode
    NextNode = NextNode + 1

def AttachRight(NodeData, ParentNode):
    global NextNode
    BinaryTree[NextNode].DataValue = NodeData
    BinaryTree[ParentNode].Right = NextNode
    NextNode = NextNode + 1
    

def print_tree(Node, BinaryTree):
    if BinaryTree is None: return
    print(BinaryTree.DataValue, end=" ")
    print_tree(BinaryTree.Left)
    print_tree(BinaryTree.Right)

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

print_tree(Node, BinaryTree)

