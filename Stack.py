class Node:
    def __init__(self, *, value = None, parent = None):
        self.value = value
        self.parent = parent

class Stack:
    def __init__(self):
        self.root = None
        self.top = self.root
    
    @property
    def top(self):
        return self._top
    
    @top.setter
    def top(self, node):
        if node == self.root:
            self._top = self.root
        else:
            self._top = node
    
    def push(self, value):
        if self.root == None:
            self.root = Node(value = value)
            self.top = self.root
        else:
            node = Node(value = value, parent = self.top)
            self.top = node
    
    def pop(self):
        if self.top.parent == None:
            self.root = None
            self.top = self.root
        else:
            self.top = self.top.parent