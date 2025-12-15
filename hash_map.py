class HashTable: #hash map is the same as hash table
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
            
        return h % self.MAX
    
    def __setitem__(self, key, val):
        index = self.get_hash(key)
        self.arr[index] = val
        
    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]
    
dic = HashTable()
# dic.add("march 6")
# dic.add("march 4")
# dic.add("march 8")
dic["march 6"] = "max amini"
print(dic["march 6"])

# print(dic.arr)
    
    