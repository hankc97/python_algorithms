class Dequeue(object):
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items = [item] + self.items

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        removed = self.items[0]
        self.items = self.items[1:]
        return removed


    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)


dequeue = Dequeue()

dequeue.add_front("hello")
dequeue.add_rear("world")

print(dequeue.remove_front() + " " + dequeue.remove_rear())
print(dequeue.size())