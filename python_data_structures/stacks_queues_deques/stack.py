class Stack:
    def __init__(self):
       self.array = [] 
    
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.array)
            
    def push(self, item):
        self.array.append(item)

    def peek(self):
        if self.size() == 0: return None
        return self.array[-1]

    def pop(self):
        return self.array.pop()





stack = Stack()
stack.push("s")
stack.pop()
print(stack.peek())
print(stack.size())

























# class Stack(object):
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []
    
#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         self.items.pop()

#     def peek(self):
#         if self.size() == 0: return None
#         return self.items[len(self.items) - 1]

#     def size(self):
#         return len(self.items)