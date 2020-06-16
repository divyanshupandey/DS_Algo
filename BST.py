
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self,root=None):
        self.root = root
    def insert(self,root,node):
        if not root:
            self.root = node
        else:
            if(node.data < root.data):
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left,node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right,node)

    def delete(self,root,data):
        if not root:
            return None
        else:
            if root.data > data:
                root.left = self.delete(root.left,data)
                return root
            elif root.data < data:
                root.right = self.delete(root.right,data)
                return root
            if(root.right==None):
                return root.left
            elif(root.left==None):
                return root.right
            else:
                prevnode = root.right
                node = root.right
                while (node.left != None):
                    prevnode = node
                    node = node.left
                if(prevnode ==  node):
                    root.right = node.right
                else:    
                    prevnode.left = node.right
                root.data = node.data
                return root
                
        
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

bst = BST()
node = Node(25)     
bst.insert(bst.root,node)
node = Node(10)     
bst.insert(bst.root,node)
node = Node(5)     
bst.insert(bst.root,node)
node = Node(15)     
bst.insert(bst.root,node)
node = Node(50)     
bst.insert(bst.root,node)
node = Node(40)     
bst.insert(bst.root,node)
node = Node(60)     
bst.insert(bst.root,node)
node = Node(35)     
bst.insert(bst.root,node)
node = Node(45)        
bst.insert(bst.root,node)
bst.root = bst.delete(bst.root,40)
bst.root = bst.delete(bst.root,100)
print(bst.root.data)
bst.inorder(bst.root)


