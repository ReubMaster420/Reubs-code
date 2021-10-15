class Node:
    def __init__(self,DataValue, LeftPointer=None, RightPointer=None):
        self.DataValue = DataValue
        self.LeftPointer = LeftPointer
        self.RightPointer = RightPointer

BinaryTree = []
for i in range(0,12):
    BinaryTree.append(node(0))
def CreateTree(NodeData):
    global NextNode
    NextNode = 0
    BinaryTree[NextNode].DataValue = NodaData
    NextNode = NextNode + 1

def AttachLeft(NodeData, ParentNode):
    BinaryTree[NextNode].DataValue = NodeData
    BinaryTree[ParentNode].LeftPointer = NextNode
    NextNode = NextNode + 1

def AttachRight(NodeData, ParentNode):
    BinaryTree[NextNode].DataValue = NodeData
    BinaryTree[ParentNode].RightPointer = NextNode
    NextNode = NextNode + 1
    
def printTreeLeft(start, traversal):
    if start:
        traversal +=(str(start.value) + "-")
        traversal = self.preorder_print(start.LeftPointer, traversal)
    return traversal
    