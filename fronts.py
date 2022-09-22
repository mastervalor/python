class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        self.head=None

    def front(self):
        if self.head:
            return self.head.value
    
    def remove(self):
        if self.head:
            self.head=self.head.next
    
    def add(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node