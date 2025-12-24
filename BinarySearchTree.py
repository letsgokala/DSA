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
        """
        Traverses the tree in the order: Left -> Root -> Right.
        In a Binary Search Tree, this visits nodes in ascending (sorted) order.
        """
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()
            
    def pre_order_traversal(self):
        """
        Traverses the tree in the order: Root -> Left -> Right.
        Useful for creating a copy of the tree or representing a structural hierarchy.
        """
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    
    def post_order_traversal(self):
        """
        Traverses the tree in the order: Left -> Right -> Root.
        Commonly used for deleting nodes or evaluating mathematical expression trees.
        """                
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)
        
    def find_max(self):
        """
        Traverse the tree and find the maximum value in the tree
        """
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def find_min(self):
        """
        Traverse the tree and find the minimum value in the tree
        """
        if self.left:
            return self.left.find_min()
        else:
            return self.data
            
    def search(self, val):
        """
        Recursively searches for a value in the tree.

        Args:
            val: The value to look for in the tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """
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
    '''
    builds our tree
    
    Args: 
        a list that contains the elements of the tree
    
    returns:
        Binary search tree
    '''
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
            
            
numbers = [17,32,65,34,1,56,2,51,54,326,23]
bst = build_tree(elements=numbers)
print(f"==================IN ORDER TRAVERSAL================")
bst.in_order_traversal()
print(f"==================PRE ORDER TRAVERSAL================")
bst.pre_order_traversal()
print(f"==================POST ORDER TRAVERSAL================")
bst.post_order_traversal()

print(f"Maximum value is - {bst.find_max()}")
print(f"Minimum value is - {bst.find_min()}")
print(bst.search(326))

    
