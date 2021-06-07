import ctypes

class DynamicArray(object):

    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.A_array = self.make_array(self.capacity)

    def __len__(self):
        return self.count
    
    def __getItem__(self, k):
        if not 0 <= k < self.count:
            return IndexError('K is out of bounds!')
        return self.A_array[k]

    def append(self, ele):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        
        self.A_array[self.count] = ele
        self.count += 1
    
    def _resize(self, new_capacity):
        B_array = self.make_array(new_capacity)

        for k in range(self.count):
            B_array[k] = self.A_array[k]
        
        self.A_array = B_array
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == '__main__':
    new_array = DynamicArray()
    new_array.append(1)
    print(len(new_array))