class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    # base case
    if root == None:
        return Node(val)

    else:
        if root.val == val:
            return root
        if root.val <= val:
            root.right = insert(root.right, val)
        if root.val >= val:
            root.left = insert(root.left, val)
    
    return root

def printInOrder(root):
    # continue to next node stack if root exists, else recurse back the stack
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)
        
root = Node(8)
insert(root, 10)
insert(root, 11)
insert(root, 4)
insert(root, 1)
insert(root, 6)

printInOrder(root)


