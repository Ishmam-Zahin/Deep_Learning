from AVL_BST_Tree import AVL_BST_Tree

class Set(AVL_BST_Tree):
    def __init__(self, allowDuplicates = False):
        super().__init__(allowDuplicates = allowDuplicates)
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def insert(self, value):
        self.add(value)
        self.size += 1
    
    def delete(self, *, node = None, value = None):
        if self.remove(node = node, value = value):
            self.size -= 1

    def begin(self):
        if self.root == None:
            return None
        
        node = self.root

        while node.left != None:
            node = node.left
        
        return node
    
    def end(self):
        node = self.root

        while node.right != None:
            node = node.right

        return node
    
    def nextNode(self, node):
        if node.right != None:
            return self.findMinNode(node.right)
        else:
            tmp = node.parent
            while tmp != None:
                if tmp.left == node:
                    break
                else:
                    node = tmp
                    tmp = tmp.parent
            
            return tmp
        
    def previousNode(self, node):
        if node.left != None:
            return self.findMaxNode(node.left)
        else:
            tmp = node.parent
            while tmp != None:
                if tmp.right == node:
                    break
                else:
                    node = tmp
                    tmp = tmp.parent
            
            return tmp



def main():
    obj = Set(allowDuplicates = False)
    obj.insert(50)
    obj.insert(75)
    obj.insert(75)
    obj.insert(25)
    obj.insert(25)
    obj.insert(30)
    obj.insert(6)
    obj.insert(60)
    obj.insert(70)
    obj.insert(52)

    while obj.begin():
        print(obj.begin().value)
        obj.delete(node = obj.begin())

    




if __name__ == "__main__":
    main()