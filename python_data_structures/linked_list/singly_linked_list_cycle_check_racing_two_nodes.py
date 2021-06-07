# Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
# You've been given the Linked List Node class code:



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(node):
    pointer1 = node
    pointer2 = node

    while pointer1 != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next

        if pointer2 == pointer1:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a # Cycle Here!

print(cycle_check(a))