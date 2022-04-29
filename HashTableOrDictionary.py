# To manually implement a Hash Table
class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]  # Internally Hash Table uses array to store values. 
        # But they are not stored sequentially. They could be stored in any order depending on the computed hash value
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):  # t["march 6"]. __getitem__ does this. This eliminates the need to call a separate function
        h = self.get_hash(index)    # like t.getItem("march 6")
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None  

t = HashTable()
t["march 6"] = 310  # Calls __setitem__
t["march 7"] = 420

t["march 6"] # Calls __getitem__
del t["march 6"] # Calls __delitem__