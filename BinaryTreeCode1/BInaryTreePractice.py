class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)

def print_tree(tree):
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

print_tree(tree)