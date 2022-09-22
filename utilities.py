class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        self.head=None

    def contains(self, value):
        runner=self.head
        while(runner):
            if runner.value == value:
                return True
            runner=runner.next
        return False

    def length(self):
        runner=self.head
        length=0
        while(runner):
            length+=1
            runner=runner.next
        return length
    
    def display(self):
        runner=self.head
        str=''
        while(runner):
            str+=f'{runner.value} here'
            runner=runner.next
        return str