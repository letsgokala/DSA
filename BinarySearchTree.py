class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)                
            else:
                self.left = BinarySearchTree(data)
        else:            
            if self.right:
                self.right.add_child(data)                
            else:
                self.right = BinarySearchTree(data)
                
    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()
            
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data: 
            if self.right:
                return self.right.search(val)
            else:
                return False
            
            
def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
            
            
numbers = [17,32,65,34,1,56,2,51,54,326,23]
bst = build_tree(elements=numbers)
bst.in_order_traversal()
print(bst.search(326))

    
