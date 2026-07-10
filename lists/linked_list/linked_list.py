# ESHAN's DATASTRUCTURES

class LinkedList():

    class Node():

        def __init__(self, val=None, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev


    def __init__(self, arr = None):

        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.size = 0 
        
        self.head.next = self.tail
        self.tail.prev = self.head

        if arr != None:
            cur = self.head
            for elem in arr:
                cur.next = self.Node(elem, None, cur)
                cur = cur.next


            cur.next = self.tail
            self.tail.prev = cur
            self.size = len(arr)


    def is_empty(self):
        return self.size <= 0
    
    def _navigate_to_node(self,index):
        closer_to_end = self.size//2 < index

        cur = self.head

        if closer_to_end:
            cur = self.tail
            cur_idx = self.size

            while cur_idx != index:
                cur_idx-=1
                cur = cur.prev
        else:
            cur_idx = -1

            while cur_idx != index:
                cur = cur.next
                cur_idx+=1

        return cur


    
    # INSERTION
    
    def append(self, value):
        self.size+=1
        self.tail.prev.next = self.Node(value, self.tail, self.tail.prev)
        self.tail.prev = self.tail.prev.next


    
    def prepend(self, value):
        self.size+=1
        self.head.next.prev = self.Node(value, self.head.next, self.head)
        self.head.next = self.head.next.prev



    def insert(self,index,value):

        if index > self.size or index < 0:
            raise IndexError('index out of bounds')

        if index == 0:
            self.prepend(value)
            return
        
        if index == self.size:
            self.append(value)
            return
        

        cur = self._navigate_to_node(index)
        

        new_node = self.Node(value,cur,cur.prev)

        cur.prev.next = new_node
        cur.prev = new_node
        self.size+=1



    # DELETION

    def pop(self):

        if self.size <=0:
            raise IndexError('popping from empty linked list')
        
        popped_node = self.tail.prev
        
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size-=1

        return popped_node.val
        


    def pop_left(self):

        if self.size <=0:
            raise IndexError('popping from empty linked list')
        
        popped_node = self.head.next
        
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size-=1

        return popped_node.val

    

    def remove(self,index):

        if index >=self.size or index < 0:
            raise IndexError('index out of bounds')
        
        if index == 0:
            return self.pop_left()
        
        if index == self.size-1:
            return self.pop()
        
        popped_node = self._navigate_to_node(index)

        cur = popped_node

        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.size-=1

        return popped_node.val
    

    # GETTERS AND SETTERS
        
    def get(self, index):
        if index >=self.size or index < 0:
            raise IndexError('index out of bounds')
        
        return self._navigate_to_node(index).val
        
    def set(self, index, value):
        if index >=self.size or index < 0:
            raise IndexError('index out of bounds')
        
        node = self._navigate_to_node(index)
        node.val = value
