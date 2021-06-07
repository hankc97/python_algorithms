class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c

    print(a.next.value)


