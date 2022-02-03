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
