class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        p = self.parent
        count = 0
        while p:
            count += 1
            p = p.parent
            
        return count
        
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    

        
electronics = TreeNode("electronics")

laptop = TreeNode("laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Hp"))
laptop.add_child(TreeNode("Dell"))

mobile = TreeNode("mobile")
mobile.add_child(TreeNode("samsung"))
mobile.add_child(TreeNode("huawei"))
mobile.add_child(TreeNode("iphone"))
mobile.add_child(TreeNode("nokia"))

ipad = TreeNode("ipad")
ipad.add_child(TreeNode("ipad1"))
ipad.add_child(TreeNode("ipad2"))
ipad.add_child(TreeNode("ipad3"))


electronics.add_child(laptop)
electronics.add_child(mobile)
electronics.add_child(ipad)

print(electronics.print_tree())

