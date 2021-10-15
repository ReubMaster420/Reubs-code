class Node(object):
    def __init__(self,DataValue, LeftPointer=None, RightPointer=None):
        self.DataValue = DataValue
        self.LeftPointer = LeftPointer
        self.RightPointer = RightPointer

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
    
    def preorder_print(self, start, traversal):
        #Root -> Left -> Right
        if start:
            traversal +=(str(start.value) + "-")
            traversal = self.preorder_print(start.LeftPointer, traversal)
            traversal = self.preorder_print(start.RightPointer, traversal)
        return traversal
        
choice = input("Do you want to input in the left or right node?")