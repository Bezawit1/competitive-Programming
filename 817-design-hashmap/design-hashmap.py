class MyHashMap(object):

    def __init__(self):
        self.hashmap={}

    def put(self, key, value):
        self.hashmap[key] = value
        
        

    def get(self, key):
        if key in self.hashmap:
            return self.hashmap[key]
        else:
            return -1
        

    def remove(self, key):
        if key in self.hashmap:
            del self.hashmap[key]
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)