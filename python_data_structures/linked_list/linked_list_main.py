class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None

def reverse(head):
    current = head
    prev = None
    next = None

    while current:
        nextnode = current.nextnode
        current.nextnode = prev
        prev = current
        current = next

    return prev

