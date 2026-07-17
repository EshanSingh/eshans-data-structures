from lists.linked_list.linked_list import LinkedList

class Queue():
    
    def __init__(self):
        self.queue = LinkedList()
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue.size != 0:
            return self.queue.pop_left()
        else:
            raise IndexError('dequeueing from empty queue')
        
    def peek(self):
        if self.queue.size != 0:
            return self.queue.get(0)
        else:
            raise IndexError('peeking from empty queue')
        
    def is_empty(self):
        return self.queue.size == 0
    
    def __len__(self):
        return self.queue.size
    


