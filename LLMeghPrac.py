class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def node_pop(self):
        #new_node = self.tail
        if self.length == 0:
            print("Nothing to pop an empty list")
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
            #only one node
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail= new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
my_linked_list.node_pop()
print("After POP")
my_linked_list.print_list()
"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3
    
"""
