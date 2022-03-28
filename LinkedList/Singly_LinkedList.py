# Step 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Step 2:
class LinkedList:
    def __init__(self):
        self.head = None

    # Step 3:
    def tranverse(self):
        if self.head is None:
            print("Linked list is empty!!!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="--->")
                n = n.ref

    # Step 4:
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Step 5:
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    # Step 6:
    def insert_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref

        if n is None:
            print("element not found!!!!!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Step 7:
    def insert_before(self, data, x):
        if self.head is None:
            print("Node is Empty!!!")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is Not Found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Step 8:
    def delete_at_begining(self):
        if self.head is None:
            print("Linked is Empty!!!!")
        else:
            self.head = self.head.ref

    # Step 9:
    def delete_at_end(self):
        if self.head is None:
            print("Linked is Empty!!!!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # Step 10:
    def delete_node(self, x):
        if self.head is None:
            print("Linked is Empty!!!!")
            return
        if self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node not present in a linked list")
            else:
                n.ref = n.ref.ref
    # Step 12:
    def length(self):
        count = 0
        if self.head is None:
            print("\n",0)
            return
        if self.head.ref is None:
            print("\n",1)
        else:
            n = self.head
            while n is not None:
                n= n.ref
                count += 1
            print("\n",count)
    
    #  Step 13
    def max_node(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head.ref
            maxi = self.head.data
            while n is not None:
                if maxi < n.data:
                    maxi = n.data
                n = n.ref
            print(maxi)
    
    #  Step 14
    def min_node(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n = self.head.ref
            mini = self.head.data
            while n is not None:
                if mini > n.data:
                    mini = n.data
                n = n.ref
            print(mini)
    
    # Step 15
    def nodes_sum(self):
        if self.head is None:
            print("LL is Empty so sum is Zero")
        else:
            n = self.head
            addn = 0
            while n is not None:
                addn += n.data
                n = n.ref
            print(addn)
    
    # Step 16
    def nodes_prod(self):
        if self.head is None:
            print("LL is Empty so product is Zero")
        else:
            n = self.head
            prodn = 1
            while n is not None:
                prodn *= n.data
                n = n.ref
            print(prodn)



sll = SinglyLinkedList()
sll.insert_begin(30)
sll.insert_begin(20)
sll.insert_begin(10)
sll.insert_end(40)
sll.insert_end(50)
sll.insert_end(60)
sll.add_after(70, 60)
sll.add_after(5, 10)
sll.add_before(2, 5)
sll.add_before(1, 2)
sll.traverse()
sll.delete_begin()
sll.delete_end()
sll.delete_by_value(60)
print("\n")
sll.traverse()
sll.length()
sll.max_node()
sll.min_node()
sll.nodes_sum()
sll.nodes_prod()
