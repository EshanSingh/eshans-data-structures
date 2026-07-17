from lists.linked_list.linked_list import LinkedList

class Stack():

    def __init__(self):
        self.stack = LinkedList()
        pass


    def push(self, item):
        self.stack.prepend(item)
    
    def pop(self):
        if self.stack.size != 0:

            return self.stack.pop_left()

        else:
             raise IndexError('popping from empty stack')

    
    def peek(self):
        if self.stack.size != 0:

            return self.stack.get(0)

        else:
             raise IndexError('peeking from empty stack')
        
    
    def is_empty(self):
        return self.stack.size == 0
    
    def __len__(self):
        return self.stack.size
