# Step 1:
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # Step 2:
    def insertion(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild is not None:
                self.lchild.insertion(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)

    # Step 3:
    def search(self, data):
        if self.key == data:
            print("Given node found ")
            return
        if data < self.key:
            if self.lchild is None:
                print("Node is Not present")
            else:
                self.lchild.search(data)
        else:
            if self.rchild is None:
                print("Node is Not present")
            else:
                self.rchild.search(data)
     # Step 4:
    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild is not None:
            self.lchild.pre_order()
        if self.rchild is not None:
            self.rchild.pre_order()
    
    # Step 5:
    def in_order(self):
        if self.lchild is not None:
            self.lchild.in_order()
        print(self.key, end=" ")
        if self.rchild is not None:
            self.rchild.in_order()

    # Step 6:
    def post_order(self):
        if self.lchild is not None:
            self.lchild.post_order()
        if self.rchild is not None:
            self.rchild.post_order()
        print(self.key, end=" ")