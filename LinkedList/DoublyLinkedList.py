# Step 1
class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


# Step 2:
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # step 3:
    def forward_tranverse(self):
        if self.head is None:
            print("Linked list is empty!!!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="--->")
                n = n.nref

    # Step 4:
    def backward_tranverse(self):
        if self.head is None:
            print("Linked list is empty!!!!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, end="<--")
                n = n.pref
        print("\n")

    # Step 5:
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    # Step 4:
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Step 5:
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    # Step 6:
    def add_after(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is Not present in Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    # Step 7:
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is Not present in Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    # Step 8:
    def delete_begin(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.nref is None:
            self.head = None
            print("LL is empty now")
        else:
            self.head = self.head.nref
            self.head.pref = None

    # Step 9:
    def delete_end(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.nref is None:
            self.head = None
            print("LL is empty now")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    # Step 10:
    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head.nref = None
                print("DLL is empty now")
                return
            else:
                print("Node is Not present")
                return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if n.data == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.ref.pref = n.pref
        else:
            if n.data == x:
                n.pref = None
            else:
                print("Node is not present in the DLL")


dll1 = DoublyLinkedList()
dll1.insert_empty(10)
dll1.insert_at_begin(20)
dll1.insert_at_end(5)
dll1.add_after(10, 20)
dll1.add_before(50, 10)
dll1.backward_tranverse()
dll1.forward_tranverse()
