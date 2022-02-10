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
    
    # Step 7
    def delete(self,data, curr):
        if self.key is None:
            print("BST is empty")
            return
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Node is Not present in a tree")
        elif data > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Node is Not present in a tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = self.rchild.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return 
                self = None
                return temp
            if self.rchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return 
                self = None
                return temp
            node = self.rchild
            while node.lchild is not None:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
            

root = BST(10)
lst = [6,3,1,6,98,3,7]
for i in lst:
    root.insertion(i)

root.search(100)
print("\nPre-order", end="\n")
root.pre_order()
print("\nIn-order", end="\n")
root.in_order()
print("\nPost-order", end="\n")
root.post_order()

print("\n After Delete")
root.delete(6)
print("\nIn-order", end="\n")
root.in_order()
