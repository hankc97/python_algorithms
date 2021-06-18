class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None  
        self.rightChild = None

root = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)
e = Node(6)
f = Node(7)
g = Node(8)

root.leftChild = a
root.rightChild = b
b.leftChild = c
a.rightChild = d
d.leftChild = e
e.leftChild = f
e.rightChild = g

# visited set are called back edges, 

def dfs(node, key,):
    if node: print(node.key)
    if node == None:
        return None
    dfs(node.leftChild)
    dfs(node.rightChild)

dfs(root)

    