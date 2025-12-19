class HashTable: #hash map is the same as hash table
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
            
        return h % self.MAX
    
    def __setitem__(self, key, val):
        index = self.get_hash(key)
        found = False
        
        for idx, element in enumerate(self.arr[index]):
            if len(element) == 2 and element[0]==key:                
                self.arr[index][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[index].append((key,val))
        
    def __getitem__(self, key):
        index = self.get_hash(key)
        
        for element in self.arr[index]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self, key):
        index = self.get_hash(key)
        
        for idx, element in enumerate(self.arr[index]):
            if element[0] == key:
                del self.arr[index][idx]
                
                
dic = HashTable()
# dic.add("march 6")
# dic.add("march 4")
# dic.add("march 8")
dic["march 6"] = 120
dic["march 8"] = 32
dic["march 9"] = 90
dic["march 17"] = 432
# print(dic.arr)
print(dic["march 6"])

del dic["march 17"]

print(dic.arr)
    
    