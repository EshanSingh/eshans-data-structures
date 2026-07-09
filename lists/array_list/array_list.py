# ESHAN's DATASTRUCTURES

class ArrayList():

    def __init__(self, starting_array=None):
        if starting_array != None:
            self.arr = list(starting_array)
            self.size = len(starting_array)
            self.capacity = self.size
        else:
            self.arr = [None]
            self.size = 0
            self.capacity = 1
    
    def _resize(self):
        self.capacity += 1
        self.capacity *= 2
        copy = [None] * self.capacity

        for i in range(self.size):
            copy[i] = self.arr[i]
        
        self.arr = copy
            


    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        
        self.arr[self.size] = value
        self.size+=1

    

    def insert(self, index, value):
        if index >= self.size or index < 0:
            raise IndexError('insertion index is out of bounds')
        
        if self.size == self.capacity:
            self._resize()
        
        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]
        self.arr[index] = value
        self.size+=1
    

    def pop(self):
        if self.size == 0:
            raise IndexError('popping from empty list')
        self.size -= 1
        return self.arr[self.size]



    
    def remove_at(self, index):
        if index >= self.size or index < 0:
            raise IndexError('removal index is out of bounds')
        for i in range(index, self.size-1):
            self.arr[i] = self.arr[i+1]
        self.size-=1


    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError('get index is out of bounds')
        return self.arr[index]


    
    def set(self, index, value):
        if index >= self.size:
            raise IndexError('set index is out of bounds')
        self.arr[index] = value