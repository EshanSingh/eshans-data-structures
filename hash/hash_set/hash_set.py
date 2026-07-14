from ..hash_map.hash_map import HashMap

class HashSet():

    def __init__(self, initial_elements):
        self.map = HashMap()

        for elem in initial_elements:
            self.map.put(elem, None)
        

    # API METHODS

    def add(self, item):
        self.map.put(item, None)
    
    def remove(self, item):
        self.map.remove(item)
    
    def discard(self, item):
        try:
            self.map.remove(item)
        except:
            pass
    
    def is_empty(self):
        return self.map.is_empty()


    # DUNDER METHODS

    def __contains__(self, item):
        try:
            self.map.get(item)
        except:
            return False
    
        return True
    
    def __len__(self):
        return self.map.size
    



