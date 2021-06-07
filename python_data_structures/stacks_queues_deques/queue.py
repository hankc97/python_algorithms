class Queue:
    def __init__(self):
        self.array = []

    def isEmpty(self):
        return self.size()

    def size(self):
        return len(self.array)

    def enqueue(self, item):
        self.array = [item] + self.array
    
    def dequeue(self):
        self.array.pop()












queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())




















# class Queue(object):
#     def __init__(self):
#         self.array = []

#     def enqueue(self, item):
#         self.array = [item] + self.array 

#     def dequeue(self):
#         return self.array.pop()

#     def isEmpty(self):
#         return self.size() == 0
    
#     def size(self):
#         return len(self.array)
    