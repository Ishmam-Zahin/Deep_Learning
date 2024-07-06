from AVL_BST_Tree import AVL_BST_Tree
import sys

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
        if self.root == None:
            return None
        
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
    print(sys.getsizeof(obj))
    obj.insert(46)
    obj.insert(47)
    obj.insert(48)
    obj.insert(49)
    print(sys.getsizeof(obj))

    




if __name__ == "__main__":
    main()