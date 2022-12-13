
class Stack:
    def __init__(self):
        self.items = []
   
    def isEmpty(self):
        # method to check the stack is empty or not
        return self.items == []
   
    def push(self, item):
        # method for pushing an item
        self.items.append(item)
        
    def pop(self):
        # method for popping an item
        return self.items.pop()
   
    def peek(self):
        # check what item is on top of the stack without removing it
        return self.items[-1]
    
    def size(self):
        # method to get the size
        return len(self.items)
    
    def fullStack(self):
        # to view the entire stack
        return self.items