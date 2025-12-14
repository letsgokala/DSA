class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, None)
        node.next = self.head
        self.head = node
        
    def print(self):
        if self.head is None:
            print("the linked list is empty")
            
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
            
        print(llstr)
            
        
    def insert_at_end(self, data):
        node = Node(data, None)
        
        if self.head is None:
            self.head = node
            
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = node
    
    def insert_values(self, data_list):
        self.head = None        
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        iteration = self.head
        while iteration:
            count += 1            
            
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count =0
        
    
    
    

if __name__ == '__main__':
    ll = LinkedList()
    
    ll2 = LinkedList()
    
    ll.insert_at_beginning(32)
    ll.insert_at_beginning(28)
    ll.insert_at_beginning(92)
    ll.insert_at_beginning(78)
    
    ll2.insert_at_end(32)
    ll2.insert_at_end(45)
    ll2.insert_at_end(56)
    ll2.insert_at_end(43)
    
    
    
    ll.print()
    print("\n")
    ll2.print()