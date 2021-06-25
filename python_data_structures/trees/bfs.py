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

def bfs(root):
    queue = [root]
    while len(queue) != 0:
        popped = queue.pop(0)
        print(popped.key)
        if popped.leftChild:
            queue.append(popped.leftChild)
        if popped.rightChild:
            queue.append(popped.rightChild)

bfs(root)