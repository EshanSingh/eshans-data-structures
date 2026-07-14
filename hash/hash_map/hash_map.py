from lists.array_list.array_list import ArrayList
from lists.linked_list.linked_list import LinkedList


LOAD_CAPACITY = 0.7

class HashMap():

    class HashNode():
        
        def __init__(self, key, val):
            self.key = key
            self.val = val

        def __eq__(self, other):
            return self.key == other.key

    def __init__(self, capacity=10):
        self.map = ArrayList([LinkedList([]) for _ in range(capacity)])
        self.capacity = capacity
        self.size = 0


    def _hash(self, key):
        return abs(hash(key))
    
    def _resize(self):
        self.capacity*=2

        old_map = self.map
        self.map = ArrayList([LinkedList([]) for _ in range(self.capacity)])

        for i in range(old_map.size):
            lst = old_map.get(i)
            cur = lst.head.next
            while cur != lst.tail:
                node = cur.val
                idx = self._hash(node.key) % self.capacity   # rehash with NEW capacity
                self.map.get(idx).append(self.HashNode(node.key, node.val))
                cur = cur.next
            
    
    def _calculate_load(self):
        return self.size/self.capacity




    # API Methods

    def is_empty(self):
        return self.size==0

    def put(self, key, value):
        hash_idx = self._hash(key) % self.capacity

        try:
            lst = self.map.get(hash_idx)
        except:
            raise KeyError('key not found')

        val_removed = lst.remove_val(self.HashNode(key,None))
        lst.append(self.HashNode(key,value))

        if not val_removed:
            self.size+=1

        if self._calculate_load() >= LOAD_CAPACITY:
            self._resize()
            
    
    def remove(self, key):
        hash_idx = self._hash(key) % self.capacity
        try:
            lst = self.map.get(hash_idx)
        except:
            raise KeyError('key not found')
        val_removed = lst.remove_val(self.HashNode(key,None))

        if val_removed:
            self.size-=1
    
    def get(self, key):
        hash_idx = self._hash(key) % self.capacity
        try:
            lst = self.map.get(hash_idx)
        except:
            raise KeyError('key not found')

        node = lst.get_by_val(self.HashNode(key,None))

        return node.val
    


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key,value)