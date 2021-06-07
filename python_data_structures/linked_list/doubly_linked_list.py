class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.prev = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.prev = a
b.next = c
c.prev = b

